from api import app
from database import Database, Engine
from config import *

with app.app_context() as context:
    Database.metadata.create_all(Engine)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)
