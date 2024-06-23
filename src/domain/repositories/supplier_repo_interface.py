from abc import ABC, abstractmethod
from domain.dtos.supplier import CreateSupplierDto
from domain.entities import SupplierEntity


class ISupplierRepository(ABC):
    @abstractmethod
    def create(self, supplier: CreateSupplierDto) -> dict[SupplierEntity] | None:
        """Create a new supplier in the database.

        Args:
            supplier (CreateSupplierDto): The supplier to be created.

        Raise:
            sqlalchemy.exc.IntegrityError: If the supplier already exists in the database.

        Returns:
            dict[SupplierEntity] | None: The supplier created or None if the supplier already exists.

        """
        pass

    @abstractmethod
    def find_all(self) -> list[dict[SupplierEntity]]:
        """Find all suppliers.

        Returns:
            list[dict[SupplierEntity]]: All suppliers found.

        """
        pass

    @abstractmethod
    def find_by_id(self, supplier_id: int) -> dict[SupplierEntity] | None:
        """Find a supplier by id.

        Args:
            supplier_id (int): The id of the supplier to find.

        Returns:
            dict[SupplierEntity] | None: The supplier found or None if the supplier does not exist.

        """
        pass

    @abstractmethod
    def update(self, supplier: SupplierEntity) -> dict[SupplierEntity] | None:
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
    def delete(self, supplier_id: int) -> dict[SupplierEntity] | None:
        """Delete a supplier from the database.

        Args:
            supplier_id (int): The id of the supplier to delete.

        Returns:
            dict[SupplierEntity] | None: The supplier deleted or None if the supplier does not exist.

        """
        pass
