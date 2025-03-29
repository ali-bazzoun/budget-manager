class User:
    def __init__(
        self,
        username: str,
        password: str,
        firstname: str | None = None,
        lastname: str | None = None,
        user_id: str | None = None
    ):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self) -> str:
        full_name = " ".join(filter(None, [self.firstname, self.lastname])) or "N/A"
        return f"User(id={self.user_id}, username={self.username}, name={full_name})"
