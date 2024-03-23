from domain.entities import UserEntity


class CreateUserDto(UserEntity):
    def __init__(self, first_name: str, last_name: str, username: str, password: str):
        super().__init__(first_name, last_name, username, password)


class UpdateUserDto(UserEntity):
    def __init__(self, id: int, first_name: str, last_name: str):
        super().__init__(first_name, last_name, None, None)
        self.id = id


class UpdateUserPasswordDto(UserEntity):
    def __init__(self, id: int, password: str):
        super().__init__(None, None, None, password)
        self.id = id


class UpdateUserUsernameDto(UserEntity):
    def __init__(self, id: int, username: str):
        super().__init__(None, None, username, None)


class UpdateUserRoleDto(UserEntity):
    def __init__(self, id: int, role: str):
        super().__init__(None, None, None, None)
        self.id = id
