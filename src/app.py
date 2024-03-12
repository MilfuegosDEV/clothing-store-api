from flask import Flask


def create_app() -> Flask:
    from db import DBConfig, db

    app = Flask(__name__)
    app.config.from_object(DBConfig)

    db.init_app(app)

    with app.app_context():
        db.create_all()
    
    return app


if __name__ == '__main__':
    app = create_app()