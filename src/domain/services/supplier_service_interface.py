from abc import ABC, abstractmethod
from domain.dtos.supplier import UpdateSupplierDto, CreateSupplierDto
from domain.entities import SupplierEntity


class ISupplierService(ABC):
    @abstractmethod
    def create(self, supplier: CreateSupplierDto) -> dict[SupplierEntity] | None:
        """Create a new supplier in the database.

        Args:
            supplier (SupplierEntity): The supplier to be created.

        Raise:
            sqlalchemy.exc.IntegrityError: If the supplier already exists in the database.

        Returns:
            dict[SupplierEntity] | None: The supplier created or None if the supplier already exists.

        """
        pass

    @abstractmethod
    def update(self, supplier: UpdateSupplierDto) -> dict[SupplierEntity] | None:
        """Update a supplier in the database.

        Args:
            supplier (SupplierEntity): The supplier to be updated.

        Raise:
            sqlalchemy.exc.IntegrityError: If the supplier already exists in the database.

        Returns:
            dict[SupplierEntity] | None: The supplier updated or None if the supplier does not exist.
        """
        pass

    @abstractmethod
    def get_details(self, ìd: str) -> dict[SupplierEntity] | None:
        """Retrieve details from a supplier by its id.

        Args:
            id (str): The id of the supplier to find.

        Returns:
            dict[SupplierEntity] | None: The supplier's details found or None if the id does not exist.

        """
        pass

    @abstractmethod
    def find_all(self) -> list[dict[SupplierEntity]]:
        """Find all suppliers.

        Returns:
            list[dict[SupplierEntity]]: A list of all suppliers.
        """
        pass

    @abstractmethod
    def change_state(self, id: int) -> dict[SupplierEntity] | None:
        """Disables a supplier by id.

        Args:
            id (str): The id of the supplier to delete.

        Returns:
            dict[SupplierEntity] | None: The supplier disabled or None if the supplier does not exist.

        """
        pass
