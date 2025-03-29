from core import HandlerContext
from handlers.base_handler import BaseHandler
from handlers.account_handler import AccountHandler
from handlers.budget_handler import BudgetHandler

class MainMenuHandler(BaseHandler):
    """Handles account/logout/exit operations"""
    
    def __init__(self, context: HandlerContext):
        super().__init__(context)
        self.account_handler = AccountHandler(context)
        self.budget_handler = BudgetHandler(context)
    
    def handle_menu(self):
        """Main menu router"""
        choice = self.menu_ui.display_main_menu(self.state.current_user.username)
        
        actions = {
            '1': lambda: self.budget_handler.handle_menu(),
            '2': lambda: self.account_handler.handle_menu(),
            '3': self._handle_logout,
            '4': self._handle_exit
        }
        
        action = actions.get(choice, self._handle_invalid_choice)
        return action() 
    
    def _handle_logout(self):
        self.feedback.display_logout_message(self.state.current_user.username)
        self.state.reset()
