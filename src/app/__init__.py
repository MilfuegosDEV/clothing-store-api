from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

def create_app(name: str) -> Flask:
    from .routes import auth    
    from config import DATABASE_CONNECTION_URI, SQLALCHEMY_TRACK_MODIFICATIONS, SEND_FILE_MAX_AGE_DEFAULT, SECRET_KEY
    from database import Engine, Database
    
    app: Flask = Flask(name)

    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = SEND_FILE_MAX_AGE_DEFAULT

    app.register_blueprint(blueprint=auth.Router(), url_prefix="/auth")

    with app.app_context() as ctx:
        Database.metadata.create_all(Engine)

    @app.errorhandler(HTTPException)
    def __not_found__(e):
        if e.code == 404:
            return jsonify({"message": "The requested url does not exists"}), e.code

        return jsonify({"message": e.description}), e.code
    return app
