from models import User
from repositories.user_repository import UserRepository


class AuthController:
    
    def __init__(self):
        self.user_repo = UserRepository()

    def login(self, username: str, password: str) -> User | None:
        result = self.user_repo.login(username, password)
        return result if result else None 
    
    def register(self, username: str, password: str, firstname: str, lastname: str) -> User | None:
        user = User(
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
        )
        result = self.user_repo.save(user)
        return self.user_repo.find_by_id(user.user_id) if result else None