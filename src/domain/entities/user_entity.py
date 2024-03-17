class UserEntity:
    def __init__(self, first_name: str, last_name: str, username: str, password: bytes):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.username: str = username
        self.password: str = password
