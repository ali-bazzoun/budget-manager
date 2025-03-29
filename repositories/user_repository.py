from sqlite3 import IntegrityError
from models.user import User
from database import execute_query


class UserRepository:

    def save(self, user: User, user_id: int | None = None) -> bool:
        """
        Saves a user to the database. If `user_id` is provided, update the existing user.
        Otherwise, insert a new user and return the new user ID.
        """
        if user_id: # Update existing user
            query = """--sql
            UPDATE users 
            SET username = ?, password = ?, firstname = ?, lastname = ? 
            WHERE id = ?
            """
            params = (user.username, user.password, user.firstname, user.lastname, user_id)
        else: # Insert new user
            query = """--sql
            INSERT INTO users (username, password, firstname, lastname) 
            VALUES (?, ?, ?, ?)
            """
            params = (user.username, user.password, user.firstname, user.lastname)

        try:
            execute_query(query, params, commit=True)
            return True
        except IntegrityError:
            print("Error: Username already exists.")
            return False
        
    def delete(self, user_id: int) -> bool:
        query = "DELETE FROM users WHERE id = ?"
        result = execute_query(query, (user_id,), commit=True)
        return result > 0

    def exists(self, user_id: int) -> bool:
        query = "SELECT COUNT(*) FROM users WHERE id = ?"
        count = execute_query(query, (user_id,), fetch_one=True)
        return count > 0
    
    def find_by_id(self, user_id: int) -> User | None:
        query = """--sql
        SELECT id, username, password, firstname, lastname
        FROM users
        WHERE id = ?
        """
        result = execute_query(query, (user_id,), fetch_one=True)
        if result:
            return User(
                user_id=result[0],
                username=result[1],
                password=result[2],
                firstname=result[3],
                lastname=result[4]
            )
        return None
    
    def login(self, username: str, password: str) -> User | None:
        query = """--sql
        SELECT id, username, password, firstname, lastname
        FROM users
        WHERE username = ? AND password = ?
        """
        result = execute_query(query, (username, password), fetch_one=True)
        if result:
            return User(
                user_id=result[0],
                username=result[1],
                password=result[2],
                firstname=result[3],
                lastname=result[4]
            )
        return None