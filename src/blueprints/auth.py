"""Set of routes for the auth blueprint"""
from flask import Blueprint, jsonify, request


bp: Blueprint = Blueprint('auth', __name__)
"""Set of routes for auth proccesses"""

@bp.route('/login')
def login():
    return jsonify({"path": '/auth/login'}), 200

@bp.route('/register')
def register():
    return jsonify({"path": "/auth/register"}), 201
