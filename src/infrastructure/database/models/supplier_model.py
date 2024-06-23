from infrastructure.extensions import db
from domain.entities import SupplierEntity
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String


class SupplierModel(db.Model):
    __tablename__ = "SUPPLIER"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    address: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)

    def __init__(self, supplier: SupplierEntity):
        self.name = supplier.name
        self.address = supplier.address
        self.email = supplier.email
        self.phone = supplier.phone

    def save(self) -> "SupplierModel":
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, supplier: SupplierEntity) -> "SupplierModel":
        self.name = supplier.name
        self.address = supplier.address
        self.email = supplier.email
        self.phone = supplier.phone
        db.session.commit()
        return self

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "email": self.email,
            "phone": self.phone,
        }

    def __repr__(self) -> str:
        return f"<Supplier {self.name}>"
