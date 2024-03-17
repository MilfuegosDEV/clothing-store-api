from flask import Flask


def create_app() -> Flask:
    from infrastructure.config import DBConfig
    from infrastructure.database import db
    from presentation.controllers import AuthController
    from presentation.errors import (
        handle_http_exception,
        handle_exception,
        HTTPException,
    )

    app = Flask(__name__)
    app.config.from_object(DBConfig)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(AuthController(), url_prefix="/auth", name="auth")
    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(Exception, handle_exception)

    return app
