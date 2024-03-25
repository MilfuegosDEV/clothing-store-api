
# Clothing Store API 🛍️
Welcome to the Clothing Store API, a RESTful API developed with Flask and SQLAlchemy using **Clean Architecture** for managing a clothing store inventory. 


![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/json%20web%20tokens-323330?style=for-the-badge&logo=json-web-tokens&logoColor=pink)


## Project Structure 🗃️
```.txt
├── src
│   ├── application
│   │   ├── external_services
│   │   └── services
│   ├── domain
│   │   ├── dtos
│   │   ├── entities
│   │   ├── repositories
│   │   └── services
│   ├── infrastructure
│   │   ├── config
│   │   ├── extensions
│   │   └── database
│   │       ├── models
│   │       └── repositories
│   ├── presentation
│   │   ├── controllers
│   │   ├── decorators
│   │   └── errors
│   └── app.py
├── .flaskenv
├── .gitignore
├── query.sql
├── README.md
└── requirements.txt
```

### Components 😖

1. ***application***: Contains business logic and services for the application, including internal and external services.
2. ***domain***: Defines entities and interfaces for the application.
3. ***infrastructure***: Manages data and external integrations, including database configuration.
4. ***presentation***: Includes controllers

## Getting Started 🦕:

To get a local copy up and running, follow these simple steps: 

1. Clone the repository:

   ```bash
   $ git clone https://github.com/milfuegosdev/clothing-store-api.git
   ```

2. Navigate to the project directory:

   ```bash
   $ cd inventory_rack
   ```

3. Install dependencies:
   ```bash
   $ pip install -r requirements.txt
   ```

4. Setup your environment: 
Create a `.flaskenv` file in the root directory of your project with the following content:

   ```makefile
   FLASK_APP=src/app.py

   DB_HOST=localhost
   DB_PORT=5432
   DB_USER=postgres
   DB_PASSWORD=admin
   DB_NAME=clothing_store

   JWT_SECRET_KEY=secret
   ```
5. Execute database setup: Execute the SQL queries in query.sql to set up your database.

Your Clothing Store API should now be up and running locally! 🚀


Feel free to explore the project and customize it according to your requirements. If you have any questions or need further assistance, don't hesitate to reach out! 🦖👕

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
