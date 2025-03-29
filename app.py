from core.context import HandlerContext
from handlers.auth_handler import AuthHandler
from handlers.main_menu_handler import MainMenuHandler

class BudgetManagerApp:
    """Main application class coordinating high-level workflow."""
    
    def __init__(self):
        self.ctx = HandlerContext()
        self.state = self.ctx.state
        self.auth_handler = AuthHandler(self.ctx)
        self.main_menu = MainMenuHandler(self.ctx)
    
    def run(self):
        """Main application loop."""
        while self.state.is_running:
            if not self.state.is_authenticated:
                self.auth_handler.handle_menu()
            else:
                self.main_menu.handle_menu()
    