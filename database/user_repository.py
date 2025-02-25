from typing import Optional, Union, List
from sqlite3 import IntegrityError
from user import User
from database.db import execute_query


def save_user(user: User, user_id: Optional[int] = None) -> Union[bool, int]:
    """
    Saves a user to the database. If `user_id` is provided, update the existing user.
    Otherwise, insert a new user and return the new user ID.
    """
    if user_id:
        query = """--sql
        UPDATE users 
        SET username = ?, password = ?, firstname = ?, lastname = ? 
        WHERE id = ?
        """
        params = (user.username, user.password, user.firstname, user.lastname, user_id)
    else:
        query = """--sql
        INSERT INTO users (username, password, firstname, lastname) 
        VALUES (?, ?, ?, ?)
        """
        params = (user.username, user.password, user.firstname, user.lastname)

    try:
        result = execute_query(query, params, commit=True)
        return result if user_id else execute_query("SELECT last_insert_rowid()", fetch_one=True)[0]
    except IntegrityError:
        print("Error: Username already exists.")
        return False


def login_user(username: str, password: str) -> Optional[User]:
    """
    Attempts to log in a user by checking their username and password.
    Returns a `User` object if authentication is successful, otherwise `None`.
    """
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


def delete_user(user_id: int) -> bool:
    """
    Deletes a user by their unique ID.
    Returns `True` if successful, `False` otherwise.
    """
    query = "DELETE FROM users WHERE id = ?"
    result = execute_query(query, (user_id,), commit=True)
    return result > 0


def list_users() -> List[User]:
    """
    Retrieves all users from the database.
    Returns a list of `User` objects.
    """
    query = "SELECT id, username, password, firstname, lastname FROM users"
    users_data = execute_query(query, fetch_all=True)
    return [
        User(
            user_id=user[0],  
            username=user[1],
            password=user[2],
            firstname=user[3],
            lastname=user[4]
        )
        for user in users_data
    ]
