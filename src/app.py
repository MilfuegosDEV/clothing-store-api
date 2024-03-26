from flask import Flask


def create_app() -> Flask:
    from flask import jsonify
    from werkzeug.exceptions import HTTPException
    from infrastructure.config import Config
    from infrastructure.extensions import db, jwt
    from infrastructure.database.models import RoleModel
    from presentation.controllers import AuthController, UserController
    from presentation.errors import (
        handle_http_exception,
        handle_exception,
        handle_unauthorized_exception,
        handle_expired_token_exception,
    )

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()
        RoleModel.SeedRoles()

    app.register_blueprint(AuthController, url_prefix="/auth", name="auth")
    app.register_blueprint(UserController, url_prefix="/users", name="users")

    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(Exception, handle_exception)

    @jwt.expired_token_loader
    def custom_expired_token_loader_callback(jwt_header, jwt_payload):
        return handle_expired_token_exception(jwt_header, jwt_payload)

    @jwt.unauthorized_loader
    def custom_unauthorized_loader_callback(error):
        return handle_unauthorized_exception(error)

    return app
