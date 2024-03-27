from application.services import SupplierService
from flask import Blueprint, jsonify, request
from domain.dtos.supplier import CreateSupplierDto, UpdateSupplierDto
from flask_jwt_extended import jwt_required

class SupplierController(Blueprint):
    def __init__(self):
        super().__init__("suppliers", __name__)
        self.supplier_service = SupplierService()

        self.add_url_rule("/get/all", view_func=self.find_all_suppliers, methods=["GET"])
        self.add_url_rule(
            "/get/<name>", view_func=self.find_supplier_by_name, methods=["GET"]
        )
        self.add_url_rule("/create", view_func=self.create_supplier, methods=["POST"])
        self.add_url_rule("/update", view_func=self.update_supplier, methods=["PUT"])
        self.add_url_rule("/delete", view_func=self.delete_supplier, methods=["DELETE"])

    @jwt_required()
    def create_supplier(
        self,
    ) -> dict | None:
        data: dict[str] = request.json

        if not all(key in data for key in ["name", "address", "email", "phone"]):
            return (
                jsonify(
                    {
                        "status": 400,
                        "message": "Invalid input data",
                        "success": False,
                        "data": None,
                    }
                ),
                400,
            )

        supplier = CreateSupplierDto(**data)

        response = self.supplier_service.create_supplier(supplier)

        if not response:
            return (
                jsonify(
                    {
                        "status": 400,
                        "message": "Supplier already exists",
                        "success": False,
                        "data": None,
                    }
                ),
                400,
            )

        return jsonify(
            {
                "status": 201,
                "success": True,
                "data": response,
            }
        )
    
    @jwt_required()
    def update_supplier(
        self,
    ) -> dict | None:
        data: dict[str] = request.json

        if not all(key in data for key in ["name", "address", "email", "phone"]):
            return (
                jsonify(
                    {
                        "status": 400,
                        "message": "Invalid input data",
                        "success": False,
                        "data": None,
                    }
                ),
                400,
            )

        supplier = UpdateSupplierDto(**data)

        response = self.supplier_service.update_supplier(supplier)

        if not response:
            return (
                jsonify(
                    {
                        "status": 404,
                        "message": "Supplier not found",
                        "success": False,
                        "data": None,
                    }
                ),
                404,
            )

        return jsonify(
            {
                "status": 200,
                "success": True,
                "data": response,
            }
        )
    
    @jwt_required()
    def find_supplier_by_name(self, name: str) -> dict | None:
        response = self.supplier_service.find_supplier_by_name(name)

        if not response:
            return (
                jsonify(
                    {
                        "status": 404,
                        "message": "Supplier not found",
                        "success": False,
                        "data": None,
                    }
                ),
                404,
            )

        return jsonify(
            {
                "status": 200,
                "success": True,
                "data": response,
            }
        )
    
    @jwt_required()
    def find_all_suppliers(self) -> dict | None:
        response = self.supplier_service.find_all_suppliers()

        if not response:
            return (
                jsonify(
                    {
                        "status": 404,
                        "message": "No suppliers found",
                        "success": False,
                        "data": None,
                    }
                ),
                404,
            )

        return jsonify(
            {
                "status": 200,
                "success": True,
                "data": response,
            }
        )
    
    @jwt_required()
    def delete_supplier(self) -> dict | None:
        data: dict[str] = request.json

        if not "name" in data:
            return (
                jsonify(
                    {
                        "status": 400,
                        "message": "Invalid input data",
                        "success": False,
                        "data": None,
                    }
                ),
                400,
            )

        name = data["name"]

        response = self.supplier_service.delete_supplier(name)

        if not response:
            return (
                jsonify(
                    {
                        "status": 404,
                        "message": "Supplier not found",
                        "success": False,
                        "data": None,
                    }
                ),
                404,
            )

        return jsonify(
            {
                "status": 200,
                "success": True,
                "data": response,
            }
        )
    