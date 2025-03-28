from controllers.user_controller import UserController
from views.menu_ui import MenuUI
from views.feedback_handler import FeedBackHandler

class AccountHandler:
    """Handles user account management workflow."""
    
    def __init__(self, state):
        self.state = state
        self.menu_ui = MenuUI()
        self.feedback = FeedBackHandler()
        self.controller = UserController()
    
    def handle_main_flow(self):
        """Main account management flow controller."""
        choice, new_value = self.menu_ui.display_user_account_menu()
        
        if choice in ['1', '2', '3', '4']:
            self._update_profile(choice, new_value)
        elif choice == '5':
            self._delete_account()
        elif choice == '6':
            self.state.in_account_menu = False
        else:
            self._handle_invalid_choice()
    
    def _update_profile(self, field_choice, new_value):
        updated = self.controller.update_profile(
            self.state.current_user,
            field_choice,
            new_value
        )
        if updated:
            self.state.current_user = updated
    
    def _delete_account(self):
        if self.controller.delete_account(self.state.current_user.user_id):
            self.state.reset()
    
    def _handle_invalid_choice(self):
        self.feedback.display_invalid_option()
        self.handle_main_flow()