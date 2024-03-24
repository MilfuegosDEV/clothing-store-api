from abc import ABC, abstractmethod
from domain.dtos.auth import LoginDto, RegisterDto
from domain.entities import UserEntity


class IAuthService(ABC):
    @abstractmethod
    def register(self, user: RegisterDto) -> dict[UserEntity]:
        """Register a new user

        Args:
            user (RegisterDto): information of the user to be registered

        Returns:
            dict[UserEntity]: the user entity created
        """
        pass

    @abstractmethod
    def authenticate(self, user: LoginDto) -> str:
        """Authenticate a user

        Args:
            user (LoginDto): user credentials

        Returns:
            str: token to be used in the authentication
        """
        pass
