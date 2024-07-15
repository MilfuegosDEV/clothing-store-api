from infrastructure.database.models import SupplierModel
from domain.repositories import ISupplierRepository
from sqlalchemy import desc, asc
import sqlalchemy.exc


class SupplierRepository(ISupplierRepository):
    def __init__(self):
        self.supplierModel = SupplierModel

    def create(self, supplier):
        if self.supplierModel.exists(phone=supplier.phone, email=supplier.email):
            raise sqlalchemy.exc.IntegrityError("Supplier already exists", None, None)
        else:
            new_supplier: SupplierModel = self.supplierModel(supplier).save()
            return new_supplier.to_dict()

    def update(self, supplier):
        if not self.supplierModel.exists(id=supplier.id):
            return None
        else:
            if self.supplierModel.exists(phone=supplier.phone, email=supplier.email):
                raise sqlalchemy.exc.IntegrityError(
                    "Supplier already exists", None, None
                )
            else:

                updated_supplier: SupplierModel = self.supplierModel.query.get(
                    supplier.id
                )
                updated_supplier.update(supplier)
                return updated_supplier.to_dict()

    def get_details(self, id):
        supplier = self.supplierModel.query.get(id)
        if supplier:
            return supplier.to_dict()
        return None

    def find_all(self):
        suppliers = self.supplierModel.query.order_by(asc(SupplierModel.id)).all()
        return [supplier.to_dict() for supplier in suppliers]

    def change_state(self, id):
        supplier = self.supplierModel.query.get(id)
        if supplier:
            return supplier.change_state().to_dict()
        return None
