from domain.services import ISupplierService
from infrastructure.database.repositories import SupplierRepository


class SupplierService(ISupplierService):
    def __init__(self):
        self.supplier_repository = SupplierRepository()

    def create(self, supplier):
        return self.supplier_repository.create(supplier)

    def update(self, supplier):
        return self.supplier_repository.update(supplier)

    def get_details(self, id):
        return self.supplier_repository.get_details(id)

    def find_all(self):
        return self.supplier_repository.find_all()

    def change_state(self, id):
        return self.supplier_repository.change_state(id)
