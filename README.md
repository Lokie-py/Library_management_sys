# Library Management System

A comprehensive web-based Library Management System built with Flask, MySQL, HTML, CSS (Bootstrap), and JavaScript.

## Features

- **Book Management**: Add, edit, delete, and view books
- **User Management**: Register and manage library members
- **Issue Books**: Issue books to users with availability tracking
- **Return Books**: Process book returns and update availability
- **Transaction History**: View all issued and returned books
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5

## Project Structure

```
/library_project
  ├── /templates
  │   ├── index.html
  │   ├── view_books.html
  │   ├── add_book.html
  │   ├── edit_book.html
  │   ├── issue_book.html
  │   ├── return_book.html
  │   ├── manage_users.html
  │   └── view_issued_books.html
  ├── /static (optional - for custom CSS/JS/images)
  ├── app.py
  ├── db.py
  ├── requirements.txt
  ├── schema.sql
  └── README.md
```

## Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- pip (Python package manager)

## Installation & Setup

### 1. Clone or Download the Project

```bash
# Create project directory
mkdir library_project
cd library_project
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup MySQL Database

**Option A: Using MySQL Command Line**
```bash
mysql -u root -p < schema.sql
```

**Option B: Using MySQL Workbench**
1. Open MySQL Workbench
2. Connect to your MySQL server
3. Open `schema.sql` file
4. Execute the SQL script

### 4. Configure Database Connection

Edit `db.py` and update the MySQL credentials:

```python
connection = mysql.connector.connect(
    host='localhost',
    database='library_db',
    user='your_mysql_username',    # Change this
    password='your_mysql_password'  # Change this
)
```

### 5. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage Guide

### Homepage
https://github.com/Lokie-py/Library_management_sys/blob/3e2cc2164b0aba36ed7e60ebc75e5f6ed1910a9e/Screenshot%202025-11-20%20220232.png
Welcome banner with gradient background
Navigation bar with links to all modules
Feature cards showcasing system capabilities
Statistics section with library metrics
Responsive design for all devices

### Managing Books
1. **View Books**: Click "View Books" to see all books in the library
2. **Add Book**: Click "Add Book" and fill in the form
3. **Edit Book**: Click the edit icon (pencil) in the books table
4. **Delete Book**: Click the delete icon (trash) in the books table

### Managing Users
1. Go to "Users" section
2. Fill in the form to add new library members
3. View all registered users in the table

### Issuing Books
1. Go to "Issue Book" section
2. Select a user from the dropdown
3. Select an available book
4. Choose the issue date
5. Click "Issue Book"

### Returning Books
1. Go to "Return Book" section
2. Select the issued book from the dropdown
3. Choose the return date
4. Click "Process Return"

### Viewing Transactions
- After issuing or returning books, you'll be redirected to the transaction history
- You can also access it directly from the Issue/Return pages

## Database Schema

### Books Table
- `book_id` (Primary Key)
- `title`
- `author`
- `genre`
- `year`
- `availability` (number of copies)

### Users Table
- `user_id` (Primary Key)
- `name`
- `email` (Unique)
- `password`

### Issued Books Table
- `issue_id` (Primary Key)
- `user_id` (Foreign Key)
- `book_id` (Foreign Key)
- `issue_date`
- `return_date`
- `status` (issued/returned)

## Features in Detail

### CRUD Operations

**Books:**
- CREATE: Add new books with title, author, genre, year, availability
- READ: View all books with their details
- UPDATE: Edit book information
- DELETE: Remove books from the system

**Users:**
- CREATE: Register new library members
- READ: View all registered users
- DELETE: Remove users from the system

**Transactions:**
- CREATE: Issue books to users
- READ: View all transactions (issued and returned)
- UPDATE: Return issued books

### Validation & Error Handling
- Form validation for required fields
- Email uniqueness check for users
- Book availability check before issuing
- Success/error flash messages
- Confirmation dialogs for delete operations

### Responsive Design
- Mobile-friendly navigation
- Responsive tables
- Bootstrap 5 styling
- Font Awesome icons
- Modern gradient design

## Troubleshooting

### Database Connection Error
- Verify MySQL is running: `sudo service mysql status`
- Check credentials in `db.py`
- Ensure database exists: `SHOW DATABASES;`

### Port Already in Use
- Change the port in `app.py`:
```python
app.run(debug=True, port=5001)
```

### Module Not Found Error
- Reinstall dependencies: `pip install -r requirements.txt`

## Security Notes

**Important for Production:**
1. Change the `secret_key` in `app.py` to a random string
2. Use environment variables for database credentials
3. Implement password hashing (e.g., bcrypt)
4. Add user authentication and authorization
5. Enable HTTPS
6. Sanitize user inputs to prevent SQL injection
7. Implement CSRF protection

## Future Enhancements

- User authentication and login system
- Password hashing and security
- Search and filter functionality
- Due date tracking and overdue notifications
- Fine calculation system
- Export data to CSV/PDF
- Book categories and tags
- Admin dashboard with statistics
- Email notifications
- Book reservation system

## Technologies Used

- **Backend**: Python, Flask
- **Database**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework**: Bootstrap 5
- **Icons**: Font Awesome 6
- **Database Connector**: mysql-connector-python

## License

This project is open-source and available for educational purposes.

## Support

For issues or questions, please check:
- MySQL documentation: https://dev.mysql.com/doc/
- Flask documentation: https://flask.palletsprojects.com/
- Bootstrap documentation: https://getbootstrap.com/

## Author

Created as a mini-project for learning web development with Flask and MySQL.

---


**Happy Coding! 📚**
