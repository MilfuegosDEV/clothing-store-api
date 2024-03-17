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
