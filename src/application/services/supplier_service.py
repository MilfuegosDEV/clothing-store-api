from domain.services import ISupplierService
from infrastructure.database.repositories import SupplierRepository

class SupplierService(ISupplierService):
    def __init__(self):
        self.repository = SupplierRepository()

    def create(self, supplier):
        return self.repository.create(supplier)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, supplier_id):
        return self.repository.find_by_id(supplier_id)

    def update(self, supplier):
        return self.repository.update(supplier)