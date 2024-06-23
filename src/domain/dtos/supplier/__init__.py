from domain.entities import SupplierEntity


class CreateSupplierDto(SupplierEntity):
    def __init__(self, name: str, address: str, email: str, phone: str):
        super().__init__(name, address, email, phone)
        self.name = name.strip().title()
        self.address = address.strip().lower()
        self.email = email.strip().lower()
        self.phone = phone.strip().lower()


class UpdateSupplierDto(SupplierEntity):
    def __init__(self, name: str, address: str, email: str, phone: str):
        super().__init__(name, address, email, phone)
        self.name = name.strip().title()
        self.address = address.strip().lower()
        self.email = email.strip().lower()
        self.phone = phone.strip().lower()
