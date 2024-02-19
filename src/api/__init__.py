from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from .routes import auth
from config import *

app: Flask = Flask(__name__)

app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = SEND_FILE_MAX_AGE_DEFAULT


app.register_blueprint(blueprint=auth.Router(), url_prefix="/auth")


@app.errorhandler(HTTPException)
def not_found(e):
    if e.code == 404:
        return jsonify({"message": "The requested url does not exists"}), e.code

    return jsonify({"message": e.description}), e.code
