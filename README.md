# Library Management System

## Student Information
* **Name:** Nadin Yasser | **ID:** 2304091
* **Name:** Mahmoud Elshaer | **ID:** 2304092
* **Course:** Introduction to Database Systems - Lab 3
* **University:** Alexandria National University, Faculty of Engineering

## Project Overview
A web-based Library Management System built using Python (Flask), MySQL, and Bootstrap. It features user authentication (Login/Register), full CRUD operations for authors and books, and relational database constraints with cascading deletes (`ON DELETE CASCADE`).

## Project Structure
```text
my-library-project/
│
├── app.py
├── problem2-DDL.sql
├── problem2-DML.sql
└── templates/
    ├── login.html
    ├── register.html
    ├── index.html
    ├── edit_author.html
    └── edit_book.html
```

## Prerequisites
Ensure you have the following installed on your system:
* Python 3
* MySQL Server / MySQL Workbench
* Required Python Libraries (`Flask`, `Flask-Bcrypt`, `PyMySQL`)

## How to Run Step by Step

### Step 1: Database Setup
1. Open **MySQL Workbench**.
2. Run the `problem2-DDL.sql` script to create the database (`library`) and tables (`users`, `author`, `book`) with foreign key constraints.
3. Run the `problem2-DML.sql` script to populate initial seed data.

### Step 2: Install Dependencies
Open your terminal in the project directory and run:
```bash
pip install Flask flask-bcrypt PyMySQL
```

### Step 3: Configure Database Connection
Open `app.py` and verify your MySQL connection settings (username and password):
```python
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='library',
        cursorclass=pymysql.cursors.DictCursor
    )
```

### Step 4: Run the Application
Execute the following command in your terminal:
```bash
python app.py
```

### Step 5: Access the Website
Open your browser and navigate to:
```text
http://127.0.0.1:5000
```
Register a new account or log in to manage authors, books, and view cascading deletions in action!
