from abc import abstractmethod
from core import HandlerContext

class BaseHandler:
    def __init__(self, context: HandlerContext):
        self.state = context.state
        self.menu_ui = context.menu_ui
        self.feedback = context.feedback

    def _handle_invalid_choice(self):
        self.feedback.display_invalid_option()

    def _handle_exit(self):
        if self.state.is_authenticated:
            self.feedback.display_exit_message(self.state.current_user.username) 
        else:
            self.feedback.display_exit_message()
        self.state.is_running = False
    
    @abstractmethod
    def handle_menu(self):
        """Display the menu and handle user input."""
        pass