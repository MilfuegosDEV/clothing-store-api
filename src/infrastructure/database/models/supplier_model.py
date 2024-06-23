from infrastructure.extensions import db
from domain.entities import SupplierEntity
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


class SupplierModel(db.Model):
    __tablename__ = "SUPPLIER"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[int] = mapped_column(String(8), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    state: Mapped[bool] = mapped_column(Boolean, default=True)

    def __init__(self, supplier: SupplierEntity):
        self.name = supplier.name
        self.address = supplier.address
        self.phone = supplier.phone
        self.email = supplier.email
        self.state = supplier.state

    def save(self) -> "SupplierModel":
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, supplier: SupplierEntity) -> "SupplierModel":
        self.name = supplier.name
        self.address = supplier.address
        self.phone = supplier.phone
        self.email = supplier.email
        db.session.commit()
        return self

    def change_state(self) -> "SupplierModel":
        self.state = not self.state
        db.session.commit()
        return self

    def to_dict(self) -> dict | None:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "state": self.state,
        }

    def __repr__(self) -> str:
        return f"<Supplier {self.name}>"

    @staticmethod
    def exists(**kwargs) -> bool:
        # Check if the supplier exists by id, phone, or email
        if kwargs.get("id"):
            return (
                True
                if SupplierModel.query.filter_by(id=kwargs.get("id")).first()
                else False
            )

        if kwargs.get("phone"):
            return (
                True
                if SupplierModel.query.filter_by(phone=kwargs.get("phone")).first()
                else False
            )

        if kwargs.get("email"):
            return (
                True
                if SupplierModel.query.filter_by(email=kwargs.get("email")).first()
                else False
            )
