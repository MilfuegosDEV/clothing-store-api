# Inventory-management ⚙️

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/json%20web%20tokens-323330?style=for-the-badge&logo=json-web-tokens&logoColor=pink)

This project is dedicated to providing a robust server application for inventory management, equipped with all the essential functionalities required for efficient inventory control.

---

## Getting Started 😎

Follow these instructions to set up the project on your local machine for development purposes.

### Clone the repository 📦

```bash
$ git clone https://github.com/MilfuegosDEV/inventory-management.git
$ cd inventory-management
```

### Create a new virtual environment for the application

```bash
$ py -m venv .venv

# in windows
$ ./.venv/Scripts/activate

# in linux
$ source .venv/bin/activate
```

> If you need more information about virtual environments, you can find it [here](https://docs.python.org/3/library/venv.html#venv-def)

### Install all required dependencies 🚀

```bash
$ pip install -r requirements.txt
```

### Create a new branch 🌿

```bash
$ git branch [branc-name]
$ git checkout -b [branch-name]
```

### Customize the configuration 🔩

```py
# sqlAchemy settings
DATABASE_CONNECTION_URI: str = "postgresql://<USERNAME>:<PASSWORD>@<HOST>:<PORT>/<DB_NAME>"

SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
SEND_FILE_MAX_AGE_DEFAULT: int = 0

# Flask settings
PORT: int = 5000
SECRET_KEY: str = "SECRET_KEY"
HOST: str = "0.0.0.0"
```

> This file is stored in [src/config/\_\_init\_\_.py](src/config/__init__.py) Feel free to modify it with your own configuration.

### Create a new database 🧑‍💻

```sql
CREATE DATABASE <DB_NAME>
```

You need to execute this query for create a new database and then include in your config `DATABASE_CONNECTION_URI` with your database name.

Now, your project is set up, and you're ready to start development.

Feel free to customize and add more sections to the README based on the specific features and functionalities of your inventory management system. Include information about database setup, API documentation, and any other relevant details. 🤖🔩
