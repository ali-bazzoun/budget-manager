from controllers.user_controller import UserController
from core import HandlerContext
from handlers.base_handler import BaseHandler

class AccountHandler(BaseHandler):
    """Handles user account management workflow."""
    
    def __init__(self, context: HandlerContext):
        super().__init__(context)
        self.controller = UserController()
    
    def handle_menu(self):
        while True:
            choice, new_value = self.menu_ui.display_user_account_menu()

            if choice == '6':
                break
            
            if choice in ['1', '2', '3', '4']:
                self._update_profile(choice, new_value)
            elif choice == '5':
                self._delete_account()
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