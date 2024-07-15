from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_jwt, verify_jwt_in_request, get_jwt_identity


def auth_required(*required_roles: str):
    """This decorator ensures that the current user is authenticated and has the required roles.

    Args:
        *required_roles: The roles required to access the endpoint.

    Example:

    >>> @auth_required("admin")
    >>> def create(self):
    """

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            logged = verify_jwt_in_request(args, kwargs)

            if not logged:
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

            if not required_roles and logged:
                # If no roles are required, just return the function
                return fn(*args, **kwargs)

            claims = get_jwt_identity()
            if claims.get("role") not in required_roles and logged:
                return (
                    jsonify(
                        {
                            "message": "You do not have permission to access this resource.",
                            "success": False,
                            "data": None,
                            "status": 403,
                        }
                    ),
                    403,
                )

            return fn(*args, **kwargs)

        return wrapper

    return decorator


__all__ = ["auth_required"]
