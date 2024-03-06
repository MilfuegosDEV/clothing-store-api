from flask import Flask
from dotenv import load_dotenv
import os

def create_app() -> Flask:
    from blueprints import bp
    from db import db
    
    load_dotenv(encoding='cp1252') # load the .env file with utf-8 encoding	

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') # get the database URI

    app: Flask = Flask(__name__) # create the Flask app
    print(SQLALCHEMY_DATABASE_URI)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI # set the database URI
    db.init_app(app)

    with app.app_context():

        db.create_all()


    app.register_blueprint(blueprint=bp, url_prefix='/api') # 
    return app