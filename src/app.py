from flask import Flask


def create_app() -> Flask:
    from core.db import DBConfig, db
    from blueprints import bp

    app = Flask(__name__)
    app.config.from_object(DBConfig)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(bp, url_prefix="/api")
    return app
