from models import User
from repositories.user_repository import UserRepository
from views.menus import FeedBackHandler

class UserController:

    def __init__(self):
        self.user_repo = UserRepository()
        self.feedback_handler = FeedBackHandler()

    def update_profile(self, user: User, choice: str, new_value: str) -> User | None:
        
        fields = {
            '1': 'username',
            '2': 'firstname',
            '3': 'lastname',
            '4': 'password'
        }

        if choice in fields:
            setattr(user, fields[choice], new_value) 
        else: return None


        if self.user_repo.save(user, user.user_id):
            return self.user_repo.find_by_id(user.user_id)
        return None
        
    
    def delete_account(self, user_id: int) -> bool:
        confirm_message = "Are you sure you want to delete your account? This action cannot be undone. (yes/no): "
        
        if self.feedback_handler.get_confirmation(confirm_message):
            result = self.user_repo.delete(user_id)
            return True if result else False
        else:
            self.feedback_handler.display_success_message("Account deletion canceled.")
            return False
    