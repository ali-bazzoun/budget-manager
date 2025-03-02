# app.py - Main application class

from views.menus import MenuUI
from views.menus import FeedBackHandler
from controllers.auth_controller import AuthController
from controllers.budget_controller import BudgetController
from controllers.user_controller import UserController
from services.budget_manager import BudgetManager

class BudgetManagerApp:
    """Main application class that orchestrates the budget management system."""
    
    def __init__(self):
        self.menu_ui = MenuUI()
        self.feedback_handler = FeedBackHandler()
        self.auth_controller = AuthController()
        self.budget_controller = BudgetController()
        self.user_controller = UserController()
        self.current_user = None
        self.budget_manager = None
        self.is_running = True
    
    def run(self):
        """Main application loop."""
        while self.is_running:
            if self.current_user is None:
                self._handle_auth_menu()
            else:
                self._handle_main_menu()
    
    def _handle_auth_menu(self):
        """Handle authentication menu flow."""
        choice = self.menu_ui.display_auth_menu()

        auth_actions = {
            '1': self._handle_registration,
            '2': self._handle_login,
            '3': self._handle_exit
        }

        action = auth_actions.get(choice, self.feedback_handler.display_invalid_option)
        action()
    
    def _handle_main_menu(self):
        """Handle main menu flow for logged-in users."""
        choice = self.menu_ui.display_main_menu(self.current_user.username)

        menu_actions = {
            '1': self._handle_budget_menu,
            '2': self._handle_account_menu,
            '3': self._handle_logout,
            '4': self._handle_exit
        }

        action = menu_actions.get(choice, self.feedback_handler.display_invalid_option)
        action()

    def _handle_budget_menu(self):
        """Handle budget menu flow for budget-related actions."""
        choice = self.menu_ui.display_budget_menu(self.budget_manager)

        budget_actions = {
            '1': self._handle_add_budget,
            '2': self._handle_view_total_summary,
            '3': self._handle_view_budget_for_month,
            '4': self._handle_edit_budget_for_month,
            '5': self._handle_main_menu
        }

        action = budget_actions.get(
            choice,
            lambda: (self.feedback_handler.display_invalid_option(), self._handle_budget_menu())
        )
        action()

    def _handle_account_menu(self):
        choice, new_value = self.menu_ui.display_user_account_menu()
        if choice in ['1', '2', '3', '4']:  # update profile
            update_result = self.user_controller.update_profile(self.current_user, choice, new_value)
            return update_result if update_result else self.current_user
        elif choice == '5':  # delete account
            if self.user_controller.delete_account(self.current_user.user_id):
                self.current_user = None
                self.budget_manager = None
                return None
            return self.current_user
        elif choice == '6':  # return to main menu
            return self.current_user
        else: # invalid option
            self.feedback_handler.display_invalid_option()
            self._handle_account_menu()

    def _handle_add_budget(self):
        """Handles adding a new budget."""
        add_budget_form = self.menu_ui.display_budget_form(self.current_user.user_id)
        self.budget_controller.create_budget(*add_budget_form)
        self.budget_manager = BudgetManager(self.current_user.user_id)

    def _handle_view_total_summary(self):
        print(self.budget_manager)
        self.feedback_handler.get_pause_message('budget menu')
        self._handle_budget_menu()

    def _handle_view_budget_for_month(self):
        print(self.budget_controller.get_budget_by_id(self.current_user.user_id, input('Month: ').lower()))
        self.feedback_handler.get_pause_message('budget menu')
        self._handle_budget_menu()


    def _handle_edit_budget_for_month(self):
        month, choice, new_value = self.menu_ui.display_budget_edit_menu()

        if choice in ['1', '2', '3', '4']:
            update_result = self.budget_controller.update_budget(
                self.current_user.user_id,
                month,
                choice,
                new_value
            )
            self.budget_manager = BudgetManager(self.current_user.user_id)
        elif choice == '5':
            if self.budget_controller.delete_budget(self.current_user.user_id, month):
                self.budget_manager = BudgetManager(self.current_user.user_id)
                return None
        return self._handle_budget_menu()


    def _handle_registration(self):
        registration_data = self.menu_ui.get_registration_details()
        self.current_user = self.auth_controller.register(*registration_data)

    def _handle_login(self):
        login_data = self.menu_ui.get_login_details()
        self.current_user = self.auth_controller.login(*login_data)
        if self.current_user:
            self.budget_manager = BudgetManager(self.current_user.user_id)

    def _handle_logout(self):
        self.feedback_handler.display_logout_message(self.current_user.username)
        self.current_user = None
        self.budget_manager = None

    def _handle_exit(self):
        self.feedback_handler.display_exit_message(self.current_user.username)
        self.is_running = False