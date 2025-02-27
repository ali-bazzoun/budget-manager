from models import User
from repositories.user_repository import UserRepository

class UserController:

    def __init__(self):
        self.user_repo = UserRepository()

    def update_profile(self, user: User, choice: str, new: str) -> User | None:
        if choice == '1':  # username
            user.username = new
        elif choice == '2':  # firstname
            user.firstname = new
        elif choice == '3':  # lastname
            user.lastname = new
        elif choice == '4':  # password
            user.password = new
        else:
            return None

        if self.user_repo.save(user, user.user_id):
            return self.user_repo.find_by_id(user.user_id)
        return None
        
    
    def delete_account(self, user_id: int) -> bool:
        result = self.user_repo.delete(user_id)
        return True if result else False
    