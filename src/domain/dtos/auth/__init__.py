from domain.entities import UserEntity
from bcrypt import hashpw, gensalt


class RegisterDto(UserEntity):
    def __init__(self, first_name: str, last_name: str, username: str, password: str):
        super().__init__(first_name, last_name, username, password)
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.username = username.strip().lower()
        self.password = hashpw(password.strip().encode(), gensalt())


class LoginDto(UserEntity):
    def __init__(self, username: str, password: str):
        super().__init__(None, None, username, password)

        self.username = username.strip().lower()
        self.password = password.strip()
