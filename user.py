from typing import Optional


class User:
    def __init__(
        self,
        username: str,
        password: str,
        firstname: Optional[str] = None,
        lastname: Optional[str] = None,
        user_id: Optional[int] = None
    ):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self) -> str:
        full_name = " ".join(filter(None, [self.firstname, self.lastname])) or "N/A"
        return f"User(id={self.user_id}, username={self.username}, name={full_name})"
