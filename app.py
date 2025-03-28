from core.app_state import AppState
from handlers.auth_handler import AuthHandler
from handlers.account_handler import AccountHandler
from handlers.budget_handler import BudgetHandler

class BudgetManagerApp:
    """Main application class coordinating high-level workflow."""
    
    def __init__(self):
        self.state = AppState()
        self.auth_handler = AuthHandler(self.state)
        self.account_handler = AccountHandler(self.state)
        self.budget_handler = BudgetHandler(self.state)
    
    def run(self):
        """Main application loop."""
        while self.state.is_running:
            if not self.state.is_authenticated:
                self.auth_handler.handle_auth_flow()
            else:
                self._handle_authenticated_flow()
    
    def _handle_authenticated_flow(self):
        """Handle post-authentication workflow."""
        handler = self._get_main_menu_handler()
        handler.handle_main_flow()
    
    def _get_main_menu_handler(self):
        return self.account_handler if self.state.in_account_menu else self.budget_handler
    