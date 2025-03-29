from core import HandlerContext
from controllers.auth_controller import AuthController
from handlers.base_handler import BaseHandler
from services.budget_manager import BudgetManager

class AuthHandler(BaseHandler):
    """Handles authentication workflow and related operations."""
    
    def __init__(self, context: HandlerContext):
        super().__init__(context)
        self.controller = AuthController()
    
    def handle_menu(self):
        """Main authentication flow controller."""
        choice = self.menu_ui.display_auth_menu()
        
        actions = {
            '1': self._handle_registration,
            '2': self._handle_login,
            '3': self._handle_exit
        }
        
        action = actions.get(choice, self._handle_invalid_choice)
        action()
    
    def _handle_registration(self):
        registration_data = self.menu_ui.get_registration_details()
        user = self.controller.register(*registration_data)
        if user:
            self.state.current_user = user
            self.state.budget_manager = BudgetManager(self.state.current_user.user_id)
        
    def _handle_login(self):
        login_data = self.menu_ui.get_login_details()
        user = self.controller.login(*login_data)
        if user:
            self.state.current_user = user
            self.state.budget_manager = BudgetManager(self.state.current_user.user_id)
    
