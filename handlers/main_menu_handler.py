from views.menu_ui import MenuUI
from core import AppState
from views.feedback_handler import FeedBackHandler
from handlers.account_handler import AccountHandler
from handlers.budget_handler import BudgetHandler

class MainMenuHandler:
    """Handles account/logout/exit operations"""
    
    def __init__(self, state: AppState):
        self.state = state
        self.menu_ui = MenuUI()
        self.feedback = FeedBackHandler()
        self.account_handler = AccountHandler(self.state)
        self.budget_handler = BudgetHandler(self.state)
    
    def handle_main_menu(self):
        """Main menu router"""
        choice = self.menu_ui.display_main_menu(self.state.current_user.username)
        
        actions = {
            '1': self._enter_budget_menu,
            '2': self._enter_account_menu,
            '3': self._handle_logout,
            '4': self._handle_exit
        }
        
        action = actions.get(choice, self._handle_invalid_choice)
        return action() 
    
    def _enter_budget_menu(self):
        self.budget_handler.handle_budget_menu()
    
    def _enter_account_menu(self):
        self.account_handler.handle_main_flow()
    
    def _handle_logout(self):
        self.feedback.display_logout_message(self.state.current_user.username)
        self.state.reset()
    
    def _handle_exit(self):
        self.feedback.display_exit_message(self.state.current_user.username)
        self.state.is_running = False
    
    def _handle_invalid_choice(self):
        self.feedback.display_invalid_option()
