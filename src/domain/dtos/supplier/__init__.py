from domain.entities import SupplierEntity


class CreateSupplierDto(SupplierEntity):
    def __init__(self, name: str, address: str, phone, email: str):
        super().__init__(name, address, phone, email)

        self.name = name.strip().title()
        self.address = address.strip().title()
        self.phone = phone
        self.email = email.strip().lower()


class UpdateSupplierDto(SupplierEntity):

    def __init__(
        self,
        id: int,
        name: str,
        address: str,
        phone: int,
        email: str,
    ):
        super().__init__(name, address, phone, email)
        self.id = id
        self.name = name.strip().title()
        self.address = address.strip().title()
        self.phone = int(phone)
        self.email = email.strip().lower()
