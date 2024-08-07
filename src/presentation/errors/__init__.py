from werkzeug.exceptions import HTTPException
from flask import jsonify


def handle_http_exception(error: HTTPException):
    return (
        jsonify(
            {
                "message": error.description,
                "success": False,
                "data": None,
                "status": error.code,
            }
        ),
        error.code,
    )


def handle_exception(error: Exception):
    return (
        jsonify(
            {
                "message": str(error),
                "success": False,
                "data": None,
                "status": 500,
            }
        ),
        500,
    )

def handle_expired_token_exception(jwt_header, jwt_payload):
    """Handles expired token exception."""
    return (
        jsonify(
            {
                "message": "Token has expired",
                "success": False,
                "data": None,
                "status": 401,
            }
        ),
        401,
    )
