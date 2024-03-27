from .auth_controller import AuthController
from .user_controller import UserController
from .supplier_controller import SupplierController

__all__ = [AuthController := AuthController(), UserController := UserController(), SupplierController := SupplierController()   ]
