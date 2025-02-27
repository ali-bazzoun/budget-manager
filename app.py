# app.py - Main application class

from views.menus import MenuUI
from views.menus import FeedBackHandler
from controllers.auth_controller import AuthController
from controllers.budget_controller import BudgetController
from controllers.user_controller import UserController

class BudgetManagerApp:
    """Main application class that orchestrates the budget management system."""
    
    def __init__(self):
        self.menu_ui = MenuUI()
        self.feedback_handler = FeedBackHandler()
        self.auth_controller = AuthController()
        self.budget_controller = BudgetController()
        self.user_controller = UserController()
        self.current_user = None
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
        
        if choice == '1':  # Register
            registration_data = self.menu_ui.get_registration_details()
            self.current_user = self.auth_controller.register(*registration_data)
        elif choice == '2':  # Login
            login_data = self.menu_ui.get_login_details()
            self.current_user = self.auth_controller.login(*login_data)
        elif choice == '3':  # Exit
            self.feedback_handler.display_exit_message()
            self.is_running = False
        else:
            self.feedback_handler.display_invalid_option()
    
    def _handle_main_menu(self):
        """Handle main menu flow for logged-in users."""
        choice = self.menu_ui.display_main_menu(self.current_user.username)
        
        if choice == '1':  # Add budget
            budget_form_month, budget_form_income, budget_form_category_percentages = self.menu_ui.display_budget_form()
            self.budget_controller.create_budget(
                self.current_user.user_id,
                budget_form_month,
                budget_form_income,
                budget_form_category_percentages
            )
        elif choice == '2':  # View budgets
            self.budget_controller.view_budgets(self.current_user)
        elif choice == '3':  # User account menu
            self.current_user = self._handle_account_menu()
        elif choice == '4':  # Logout
            self.feedback_handler.display_logout_message(self.current_user.username)
            self.current_user = None
        elif choice == '5':  # Exit
            self.feedback_handler.display_exit_message(self.current_user.username)
            self.is_running = False
        else:
            self.feedback_handler.display_invalid_option()

    def _handle_account_menu(self):
        choice = self.menu_ui.display_user_account_menu()

        if choice in ['1', '2', '3', '4']:  # Edit user
            update_result = self.user_controller.update_profile(self.current_user, choice, input('New: '))
            return update_result if update_result else self.current_user
        elif choice == '5':  # Delete account
            if self.user_controller.delete_account(self.current_user.user_id):
                return None
        elif choice == '6':  # Return to main menu
            return self.current_user
        else:
            self.feedback_handler.display_invalid_option()
            return self._handle_account_menu()