from domain.entities import UserEntity

class CreateUserDto(UserEntity):
    def __init__(self, first_name: str, last_name: str, username: str, password: str):
        super().__init__(first_name, last_name, username, password)

        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()
        self.username = username.strip().lower()
        self.password = password.strip()


class UpdateUserDto(UserEntity):

    def __init__(self, username: str, first_name: str, last_name: str):
        super().__init__(first_name, last_name, username, None)
        self.username = username.strip().lower()
        self.first_name = first_name.strip().title()
        self.last_name = last_name.strip().title()


class UpdateUserRoleDto(UserEntity):

    def __init__(self, id: int, rid: int):
        super().__init__(None, None, None, None)
        self.id = id
        self.rid = rid
