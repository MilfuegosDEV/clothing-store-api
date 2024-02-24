from app import create_app
from config import HOST, PORT

if __name__ == '__main__':
    app = create_app(__name__)
    app.run(HOST, PORT, debug=False)