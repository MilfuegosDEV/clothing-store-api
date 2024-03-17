from abc import ABC, abstractmethod
from domain.entities import UserEntity


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: UserEntity) -> dict[UserEntity] | None:
        """Create a new user in the database.

        Args:
            user (UserEntity): The user to be created.

        Raise:
            sqlalchemy.exc.IntegrityError: If the user already exists in the database.

        Returns:
            dict[UserEntity] | None: The user created or None if the user already exists.

        """
        pass
