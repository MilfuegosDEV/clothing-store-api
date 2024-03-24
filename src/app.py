from flask import Flask


def create_app() -> Flask:
    from werkzeug.exceptions import HTTPException
    from infrastructure.config import DBConfig
    from infrastructure.database import db
    from infrastructure.database.models import Role
    from infrastructure.presentation.controllers import AuthController, UserController
    from infrastructure.presentation.errors import (
        handle_http_exception,
        handle_exception,
    )

    app = Flask(__name__)
    app.config.from_object(DBConfig)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        Role.SeedRoles()

    app.register_blueprint(AuthController, url_prefix="/auth", name="auth")
    app.register_blueprint(UserController, url_prefix="/users", name="users")

    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(Exception, handle_exception)

    return app
