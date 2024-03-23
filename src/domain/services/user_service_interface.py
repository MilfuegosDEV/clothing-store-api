from abc import ABC, abstractmethod
from ..repositories import IUserRepository
from domain.entities import UserEntity


class IUserService(ABC):
    @abstractmethod
    def __init__(self, user_repository: IUserRepository = None):
        pass

    @abstractmethod
    def create_user(self, user: UserEntity) -> dict | None:
        """
        Create a new user in the database.

        Args:
            user (UserEntity): The user to be created.

        Raise:
            sqlalchemy.exc.IntegrityError: If the user already exists in the database.

        Returns:
            dict[UserEntity] | None: The user created or None if the user already exists.
        """
        pass

    # @abstractmethod
    # def update_user(self, id: int, user: UserEntity) -> dict | None:
    #     """
    #     Update a user in the database.

    #     Args:
    #         id (int): The ID of the user to be updated.
    #         user (UserEntity): The user to be updated.

    #     Returns:
    #         dict[UserEntity] | None: The user updated or None if the user does not exist.
    #     """
    #     pass

    # @abstractmethod
    # def delete_user(self, id: int) -> dict | None:
    #     """
    #     Delete a user from the database.

    #     Args:
    #         id (int): The ID of the user to be deleted.

    #     Returns:
    #         dict[UserEntity] | None: The user deleted or None if the user does not exist.
    #     """
    #     pass

    @abstractmethod
    def find_user_by_username(self, username: str) -> dict | None:
        """
        Find a user by username.

        Args:
            username (str): The username of the user to find.

        Returns:
            dict[UserEntity] | None: The user found or None if the user does not exist.
        """
        pass

    # @abstractmethod
    # def find_user_by_id(self, id: int) -> dict | None:
    #     """
    #     Find a user by ID.

    #     Args:
    #         id (int): The ID of the user to find.

    #     Returns:
    #         dict[UserEntity] | None: The user found or None if the user does not exist.
    #     """
    #     pass

    # @abstractmethod
    # def find_all_users(self) -> list[dict] | None:
    #     """
    #     Find all users.

    #     Returns:
    #         list[dict[UserEntity]]: All users found.
    #     """
    #     pass

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

    # def change_user_role(self, user_id: int, role_id: int) -> dict | None:
    #     """
    #     Change the role of a user.

    #     Args:
    #         user_id (int): The ID of the user.
    #         role_id (int): The ID of the role.

    #     Returns:
    #         dict | None: The user with the new role or None if the user does not exist.
    #     """
    #     pass
