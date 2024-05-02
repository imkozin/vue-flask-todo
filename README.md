# Todo App Manager

## Table of Contents
- [Description](#desciption)
- [Technologies Used](#technologies-Used)
- [Features](#features)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contribute](#contribute)

## Description

Todo App Manager is a full-stack web application built with Flask for the backend, Vue 3 for the frontend, and styled with vanilla CSS. The application allows users to create, edit, delete, and mark todo items as completed. It provides a simple and intuitive interface for managing tasks

## Technologies Used

- **Backend:** 
  - **Flask:** A Python web framework for building the backend.
  - **ElephantSQL:** Online database used for storing user information.
- **Frontend:** 
  - **Vue 3:** JavaScript framework for building user interfaces.

## Features

- Create new todo items
- Edit existing todo items
- Delete todo items
- Mark todo items as completed


## Configuration
### Backend and API
   The backend of the Flask-Vue-App serves as the server-side component responsible for handling HTTP requests, managing the PostgreSQL database, and serving data to the frontend. This section provides details on how to connect to the database, the technologies used, and an overview of the API endpoints.
   - ### PostgreSQL Database
   The backend of this project uses a PostgreSQL relational database to store and manage user and organization data. PostgreSQL is a powerful, open-source relational database system known for its reliability and performance. You can find the database connection information in the app.py file.
   - ### Database Configuration
   To connect to the PostgreSQL database, update the database connection details in the Flask application configuration. The database connection is configured in the app.py file. The application uses the SQLAlchemy library to interact with the database. Here's an example of the database configuration:

    ```
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    import os
    # Load environment variables from .env file
    load_dotenv()

    # create the app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    # this variable, db, will be used for all SQLAlchemy commands
    db = SQLAlchemy(app)
    ```

Replace DATABASE_URL with your variable name from .env file os.environ.get('*DATABASE_URL*') or you can give a direct link with your PostgreSQL connection details, including the username, password, host, port, and database name e.g. 

    ```
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/your-database-name'
    ``` 
    
### Frontend
The frontend of the Flask-Vue-App is built using the popular JavaScript library Vue. Vue allows for the development of dynamic and responsive user interfaces. This section provides an overview of the frontend architecture, the technologies used, and how to run the frontend application.
   - ### Frontend Architecture
   The frontend of this project follows a component-based architecture, where the user interface is divided into modular components that can be reused and combined to build complex views. Here are some key components used in the frontend:
   - **Navbar:** The navigation bar component displayed at the top of the application. It provides navigation links.
   - **Home:** The start page where users can see and manage list of planned tasks.
   - 
## Getting Started
### Prerequisites
Before running the project, make sure you have the following prerequisites:

- Python (>=3.7)
- Node.js (>=12)
- npm (Node Package Manager)
- Flask
- Vue

### Installation
To get started, follow these steps:

- Clone the repository:
```
git clone https://github.com/imkozin/vue-flask-todo.git
```
- Navigate to the project directory:
   - cd backend
   - Running the Backend
   - Create a Virtual Environment (Optional): It's recommended to create a virtual environment to isolate your project dependencies. You can do this using the venv module that comes with Python. Open your terminal and run: python -m venv venv

- Install Python dependencies:
```
pip install -r requirements.txt
```

Once the dependencies are installed, you can start the development server by running:
```
python3 app.py
```

- Running the Frontend
To run the frontend of the Flask-Vue-App locally, follow these steps:
   - Make sure you have Node.js installed on your system.
   - Navigate to the frontend directory in your project folder using the terminal.
   - Install the required dependencies by running the following command:
    ```
    npm install
    ```
   - Once the dependencies are installed, you can start the development server by running:
   ```
   npm run dev
   ```
This will launch the development server, and your Vue application will be available in your web browser at http://localhost:5173.

## Usage
- Register a new user.
- Log in to have access to the product management features.
- Edit product details or add new products.
- Manage product list by adding, editing and removing products.

## Possible improvements

1. **Add the registration system:** User session management can improve user experience and security. These additions can simplify account recovery and user authentication.
3. **Role-Based Access Control:** Define different user roles with varying levels of access permissions to control data access and manipulation.

## Contribute
Contributions are welcome! If you'd like to contribute to this project, please follow these steps described in [Configuration](#configuration). Feel free to report issues, suggest enhancements, or submit pull requests to help us improve this application.



