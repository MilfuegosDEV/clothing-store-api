from abc import ABC, abstractmethod
from domain.dtos.user import CreateUserDto, UpdateUserDto
from domain.entities import UserEntity


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: CreateUserDto) -> dict[UserEntity] | None:
        """Create a new user in the database.

        Args:
            user (UserEntity): The user to be created.

        Raise:
            sqlalchemy.exc.IntegrityError: If the user already exists in the database.

        Returns:
            dict[UserEntity] | None: The user created or None if the user already exists.

        """
        pass

    @abstractmethod
    def update(self, id: int, user: UpdateUserDto) -> dict[UserEntity] | None:
        """Update a user in the database.

        Args:
            id (int): The ID of the user to be updated.
            user (UserEntity): The user to be updated.

        Raise:
            sqlalchemy.exc.IntegrityError: If the user already exists in the database.

        Returns:
            dict[UserEntity] | None: The user updated or None if the user does not exist.
        """
        pass

    @abstractmethod
    def find_by_username(self, username: str) -> dict | None:
        """Find a user by username.

        Args:
            username (str): The username of the user to find.

        Returns:
            dict[UserEntity] | None: The user found or None if the user does not exist.

        """
        pass

    @abstractmethod
    def find_all(self) -> list[dict[UserEntity]]:
        """Find all users.

        Returns:
            list[dict[UserEntity]]: A list of all users.

        """
        pass

    # @abstractmethod
    # def find_all_by_role(self, role_id: int) -> list[dict[UserEntity]]:
    #     """Find all users by role.

    #     Args:
    #         role_id (int): The ID of the role.

    #     Returns:
    #         list[dict[UserEntity]]: A list of all users with the specified role.

    #     """
    #     pass
