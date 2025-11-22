# Library Management System

A simple web-based Library Management System built with Flask, MySQL, HTML (Bootstrap), and JavaScript. This project demonstrates basic CRUD operations for books and users, issuing/returning books, and transaction history.

Table of Contents
- Features
- Demo / Screenshots
- Prerequisites
- Installation
  - 1. Clone
  - 2. Create virtual environment
  - 3. Install dependencies
  - 4. Configure database (recommended via .env)
  - 5. Create database schema
  - 6. Run the app
- Usage
- Database schema (overview)
- Security notes
- Troubleshooting
- Future enhancements
- Contributing & License
- Author

## Features
- Book management: add, edit, delete, view
- User management: register and manage members
- Issue / return books with availability tracking
- Transaction history: view issued and returned books
- Responsive UI using Bootstrap 5

## Demo / Screenshots
Below are the screenshots you previously uploaded — I kept the original links so the images remain the same in the README.

Homepage

![Homepage](https://github.com/Lokie-py/Library_management_sys/blob/3e2cc2164b0aba36ed7e60ebc75e5f6ed1910a9e/Screenshot%202025-11-20%20220232.png)

Managing Books

![View Books](https://github.com/Lokie-py/Library_management_sys/blob/7ffcb0975f26fdd11a8e0180c250e8c13b20b4ca/Screenshot%202025-11-20%20220254.png)

Managing Users

![Manage Users](https://github.com/Lokie-py/Library_management_sys/blob/7ffcb0975f26fdd11a8e0180c250e8c13b20b4ca/Screenshot%202025-11-20%20220320.png)

Issuing Books

![Issue Book](https://github.com/Lokie-py/Library_management_sys/blob/7ffcb0975f26fdd11a8e0180c250e8c13b20b4ca/Screenshot%202025-11-20%20220344.png)

Returning Books

![Return Book](https://github.com/Lokie-py/Library_management_sys/blob/e5239bc2856fc60ca7f9f3bfce9d7c49f8f3b082/Screenshot%202025-11-22%20235956.png)

## Prerequisites
- Python 3.8+
- MySQL 8+
- pip
- (Optional) virtualenv or venv

## Installation

### 1. Clone
```bash
git clone https://github.com/Lokie-py/Library_management_sys.git
cd Library_management_sys
```

### 2. Create virtual environment
```bash
python -m venv .venv
# On macOS / Linux
source .venv/bin/activate
# On Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies
Make sure requirements.txt exists. Example requirements (add these to requirements.txt):
```
Flask>=2.0
mysql-connector-python>=8.0
python-dotenv>=1.0
```
Then:
```bash
pip install -r requirements.txt
```

### 4. Configure database (recommended via .env)
Create a `.env` file in project root (do NOT commit it):
```
FLASK_ENV=development
FLASK_APP=app.py
SECRET_KEY=replace-with-a-random-string
DB_HOST=localhost
DB_NAME=library_db
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
```
Update `db.py` to read credentials from environment variables (use python-dotenv or os.environ).

### 5. Create database schema
Import the schema:
```bash
mysql -u root -p < schema.sql
# or open schema.sql in MySQL Workbench and execute
```
Confirm a database named `library_db` or change DB_NAME in .env and schema.sql to match your preference.

### 6. Run the app
Option A — direct:
```bash
python app.py
```
Option B — using flask:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --port 5000
```
Open http://localhost:5000

## Usage
- Visit the navigation links to add/view books and users
- Issue a book only when availability > 0; returning a book increases availability
- Transaction page shows issued/returned history

## Database schema (overview)
- books (book_id PK, title, author, genre, year, availability INT)
- users (user_id PK, name, email UNIQUE, password)
- issued_books (issue_id PK, user_id FK, book_id FK, issue_date, return_date, status)

Add explicit SQL types in schema.sql (INT, VARCHAR, DATE, etc.) and foreign key constraints for referential integrity.

## Security notes
- Never store plaintext passwords. Use a password hashing library (bcrypt or passlib).
- Use environment variables for secrets and DB credentials.
- Use prepared statements or ORM (SQLAlchemy) to avoid SQL injection.
- Enable CSRF protection for forms (Flask-WTF or other middleware) before production.
- Use HTTPS in production, ensure SECRET_KEY is strong and private.

## Troubleshooting
- Database connection error: check MySQL is running and credentials in `.env`.
- Module not found: ensure venv is activated and dependencies installed.
- Port in use: run app on a different port (e.g., 5001).

## Future enhancements
- Authentication and role-based access (admin vs member)
- Password hashing + login system
- Search and filters, due date reminders, email notifications
- Dockerfile / docker-compose for easy setup
- Tests and CI workflow

## Contributing & License
If you want contributions:
1. Fork the repo
2. Create a feature branch
3. Open a PR with a clear description

Add a LICENSE (e.g., MIT) to make the project’s license explicit.

## Author
Created as a mini-project for learning web development with Flask and MySQL.

Happy Coding!
