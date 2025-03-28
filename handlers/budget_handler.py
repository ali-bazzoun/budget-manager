from controllers.budget_controller import BudgetController
from views.menu_ui import MenuUI
from views.feedback_handler import FeedBackHandler

class BudgetHandler:
    """Handles budget management workflow and operations."""
    
    def __init__(self, state):
        self.state = state
        self.menu_ui = MenuUI()
        self.feedback = FeedBackHandler()
        self.controller = BudgetController()
    
    def handle_main_flow(self):
        """Main budget management flow controller."""
        choice = self.menu_ui.display_main_menu(self.state.current_user.username)
        
        actions = {
            '1': self._handle_budget_operations,
            '2': self._enter_account_menu,
            '3': self._handle_logout,
            '4': self._handle_exit
        }
        
        action = actions.get(choice, self._handle_invalid_choice)
        action()
    
    def _handle_budget_operations(self):
        choice = self.menu_ui.display_budget_menu(self.state.budget_manager)
        
        actions = {
            '1': self._add_budget,
            '2': self._display_summary,
            '3': self._view_budget_month,
            '4': self._edit_budget_month,
            '5': self.handle_main_flow
        }
        
        action = actions.get(choice, self._handle_invalid_choice)
        print(f'\nYou selected option {choice}')
        action()
    
    def _add_budget(self):
        budget_data = self.menu_ui.display_budget_form(self.state.current_user.user_id)
        self.controller.create_budget(*budget_data)
        self._refresh_budget_manager()
    
    def _display_summary(self):
        print(self.state.budget_manager)
        self.feedback.get_pause_message('budget menu')
        self._handle_budget_operations()

    def _view_budget_month(self):
        print(self.controller.get_budget_by_id(self.state.current_user.user_id, input('Month: ').lower()))
        self.feedback.get_pause_message('budget menu')

    def _edit_budget_month(self):
        month, choice, new_value = self.menu_ui.display_budget_edit_menu()

        if choice in ['1', '2', '3', '4']:
            update_result = self.controller.update_budget(
                self.state.current_user.user_id,
                month,
                choice,
                new_value
            )
        elif choice == '5':
            if self.controller.delete_budget(self.state.current_user.user_id, month):
                return None
    
    def _enter_account_menu(self):
        self.state.in_account_menu = True
    
    def _handle_logout(self):
        self.feedback.display_logout_message(self.state.current_user.username)
        self.state.reset()
    
    def _handle_exit(self):
        self.feedback.display_exit_message(self.state.current_user.username)
        self.state.is_running = False
    
    def _refresh_budget_manager(self):
        from services.budget_manager import BudgetManager
        self.state.budget_manager = BudgetManager(self.state.current_user.user_id)
    
    def _handle_invalid_choice(self):
        self.feedback.display_invalid_option()
        self.handle_main_flow()
