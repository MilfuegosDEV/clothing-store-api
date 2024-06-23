from infrastructure.database.models import SupplierModel
from domain.repositories import ISupplierRepository
from domain.entities import SupplierEntity
from sqlalchemy import asc
import sqlalchemy.exc


class SupplierRepository(ISupplierRepository):

    def __init__(self):
        self.supplierModel = SupplierModel

    def create(self, supplier: SupplierEntity):
        try:

            new_supplier: dict[SupplierModel] | None = (
                self.supplierModel(supplier).save().to_dict()
            )
            return new_supplier

        except sqlalchemy.exc.IntegrityError:
            return None

    def update(self, supplier: SupplierEntity):
        try:
            found_supplier: SupplierModel = self.supplierModel.query.filter_by(
                name=supplier.name
            ).first()
            if not found_supplier:
                return None

            return found_supplier.update(supplier).to_dict()

        except sqlalchemy.exc.IntegrityError:
            return None

    def find_by_id(self, supplier_id):
        try:
            supplier: SupplierModel = self.supplierModel.query.filter_by(
                id=supplier_id
            ).first()

            if not supplier:
                return None

            return supplier.to_dict()

        except sqlalchemy.exc.IntegrityError:
            return None

    def find_by_name(self, name):
        try:
            supplier: SupplierModel = self.supplierModel.query.filter_by(
                name=name
            ).first()

            if not supplier:
                return None

            return supplier.to_dict()

        except sqlalchemy.exc.IntegrityError:
            return None

    def find_all(self):
        try:
            suppliers: list[SupplierModel] = self.supplierModel.query.order_by(
                asc(SupplierModel.id)
            ).all()

            if not suppliers:
                return None

            return [supplier.to_dict() for supplier in suppliers]

        except sqlalchemy.exc.IntegrityError:
            return None

    def delete(self, name):
        try:
            supplier: SupplierModel = self.supplierModel.query.filter_by(
                name=name
            ).first()

            if not supplier:
                return None

            supplier.delete()
            return supplier.to_dict()

        except sqlalchemy.exc.IntegrityError:
            return None
