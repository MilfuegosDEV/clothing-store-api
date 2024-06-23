from domain.entities import SupplierEntity
from domain.dtos.supplier import CreateSupplierDto

from abc import ABC, abstractmethod


class ISupplierService(ABC):

    @abstractmethod
    def create(self, supplier: CreateSupplierDto) -> dict[SupplierEntity] | None:
        """Create a new supplier.

        Args:
            supplier (CreateSupplierDto): The supplier to be created.

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
        """Update a supplier.

        Args:
            supplier (SupplierEntity): The supplier to be updated.

        Returns:
            dict[SupplierEntity] | None: The supplier updated or None if the supplier does not exist.

        """
        pass
