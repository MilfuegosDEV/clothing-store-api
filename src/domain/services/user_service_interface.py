from abc import ABC, abstractmethod
from domain.repositories import IUserRepository
from domain.entities import UserEntity
from domain.dtos.user import CreateUserDto, UpdateUserDto


class IUserService(ABC):
    @abstractmethod
    def __init__(self, user_repository: IUserRepository = None):
        pass

    @abstractmethod
    def update_user(self, id: int, user: UpdateUserDto) -> dict[UserEntity] | None:
        """
        Update a user in the database.

        Args:
            id (int): The ID of the user to be updated.
            user (UserEntity): The user to be updated.

        Returns:
            dict[UserEntity] | None: The user updated or None if the user does not exist.
        """
        pass

    @abstractmethod
    def find_user_by_username(self, username: str) -> dict | None:
        """
        Find a user by username.

        Args:
            username (str): The username of the user to find.
            include_password (bool): Whether to include the password in the result.

        Returns:
            dict[UserEntity] | None: The user found or None if the user does not exist.
        """
        pass

    @abstractmethod
    def find_all_users(self) -> list[dict] | None:
        """
        Find all users.

        Returns:
            list[dict[UserEntity]]: All users found.
        """
        pass

    # @abstractmethod
    # def find_all_users_by_role(self, role_id: int) -> list[dict] | None:
    #     """
    #     Find all users by role.

    #     Args:
    #         role_id (int): The ID of the role.

    #     Returns:
    #         list[dict[UserEntity]]: All users found by role.
    #     """
    #     pass
