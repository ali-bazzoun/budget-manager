from controllers.auth_controller import AuthController
from views.menu_ui import MenuUI
from views.feedback_handler import FeedBackHandler

class AuthHandler:
    """Handles authentication workflow and related operations."""
    
    def __init__(self, state):
        self.state = state
        self.menu_ui = MenuUI()
        self.feedback = FeedBackHandler()
        self.auth_controller = AuthController()
    
    def handle_auth_flow(self):
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
        self.state.current_user = self.auth_controller.register(*registration_data)
    
    def _handle_login(self):
        login_data = self.menu_ui.get_login_details()
        user = self.auth_controller.login(*login_data)
        if user:
            self.state.current_user = user
            self._initialize_budget_manager()
    
    def _handle_exit(self):
        self.feedback.display_exit_message()
        self.state.is_running = False
    
    def _handle_invalid_choice(self):
        self.feedback.display_invalid_option()
        self.handle_auth_flow()
    
    def _initialize_budget_manager(self):
        if self.state.current_user:
            from services.budget_manager import BudgetManager
            self.state.budget_manager = BudgetManager(self.state.current_user.user_id)