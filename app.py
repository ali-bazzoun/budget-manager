from core.app_state import AppState
from handlers.auth_handler import AuthHandler
from handlers.main_menu_handler import MainMenuHandler

class BudgetManagerApp:
    """Main application class coordinating high-level workflow."""
    
    def __init__(self):
        self.state = AppState()
        self.auth_handler = AuthHandler(self.state)
        self.main_menu = MainMenuHandler(self.state)
    
    def run(self):
        """Main application loop."""
        while self.state.is_running:
            if not self.state.is_authenticated:
                self.auth_handler.handle_auth_flow()
            else:
                self.main_menu.handle_main_menu()
    