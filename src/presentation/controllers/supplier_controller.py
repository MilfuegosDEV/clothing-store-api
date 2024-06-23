
import re

from flask import Blueprint, jsonify, request

from application.services import SupplierService
from domain.dtos.supplier import UpdateSupplierDto, CreateSupplierDto
from flask_jwt_extended import jwt_required


class SupplierController(Blueprint):
    def __init__(self):
        super().__init__("suppliers", __name__)
        self.supplier_service = SupplierService()

        self.add_url_rule("/create", view_func=self.create, methods=["POST"])
        self.add_url_rule("/update/:id", view_func=self.update, methods=["PUT"])
        self.add_url_rule("/get/all", view_func=self.get_all, methods=["GET"])
        self.add_url_rule("/change-state/<id>", view_func=self.change_supplier_state, methods=['PATCH'])

    @jwt_required(fresh=True)
    def create(self):
        data: dict[str, any] = request.json

        if not all(key for key in ["name", "phone", "address", "email"]):
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
            
        if not(len(data['phone']) == 8):
            return (jsonify({"status": 400, 'message':"The phone number must have 8 digits at least", "success": False, "data": None}))
        if not (data['phone'].isnumeric()):
            return (jsonify({"status": 400, 'message':"Invalid phone number", "success": False, "data": None}), 400)
        
        if not (re.match(r'/[^\s]*@[a-z0-9.-]*/i',data['email']) == None):
            return (jsonify({"status": 400, 'message': 'Invalid email address', "success": False, "data": None}), 400)

        supplier = CreateSupplierDto(**data)

        response = self.supplier_service.create(supplier)

        if response:
            return jsonify(
                {
                    "status": 201,
                    "message": "Supplier created successfully",
                    "success": True,
                    "data": response,
                }
            ), 201

        return jsonify(
            {
                "status": 409,
                "message": "Supplier already exists",
                "success": False,
                "data": None,
            }
        ), 409

    @jwt_required(fresh=True)
    def update(self, id):

        data: dict[str] = request.json
        data["id"] = id

        if not all(key in data for key in ["id", "name", "phone", "email", "address"]):
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
        response = self.supplier_service.update(supplier)

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

    @jwt_required(fresh=True)
    def change_supplier_state(self, id:int):
        response = self.supplier_service.change_state(id)

        if not response:
            return jsonify(
                {"status": 404, "message": "Supplier not found", "success": False}
            ), 404

        return jsonify({"status": 200, "message": f"Supplier {"enabled" if response['state'] else "disabled"} successufully", "success": True})

    @jwt_required(fresh=True)
    def get_all(self):
        data: list[dict[str, any]] = self.supplier_service.find_all()

        if not data or len(data) == 0:
            return (jsonify(
                {
                    "status": 404,
                    "message": "Suppliers not found",
                    "success": False,
                }
            ),404)

        return jsonify({"status": 200, "success": True, "data": data})
