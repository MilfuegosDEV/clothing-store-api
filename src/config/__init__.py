# sqlAchemy settings
DATABASE_CONNECTION_URI: str = "postgresql://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>"
SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
SEND_FILE_MAX_AGE_DEFAULT: int = 0

# Flask settings
PORT: int = 8080
SECRET_KEY: str = ''
HOST: str = '0.0.0.0'

