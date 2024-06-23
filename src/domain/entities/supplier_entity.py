class SupplierEntity:
    def __init__(
        self, name: str, email: str, phone: str, address: str, state: bool = True
    ):
        self.name: str = name
        self.email: str = email
        self.phone: str = phone
        self.address: str = address
        self.state: bool = state
