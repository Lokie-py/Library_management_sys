from flask import Flask, render_template, request, redirect, url_for, flash
from db import execute_query
from datetime import datetime

app = Flask(__name__)
app.secret_key = '123456789'

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# View all books
@app.route('/view_books')
def view_books():
    query = "SELECT * FROM books ORDER BY book_id DESC"
    books = execute_query(query, fetch=True)
    return render_template('view_books.html', books=books)

# Add new book - BOTH GET and POST
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        genre = request.form.get('genre')
        year = request.form.get('year')
        availability = request.form.get('availability')
        
        if not title or not author:
            flash('Title and Author are required!', 'danger')
            return redirect(url_for('add_book'))
        
        query = """INSERT INTO books (title, author, genre, year, availability) 
                   VALUES (%s, %s, %s, %s, %s)"""
        params = (title, author, genre, year, availability)
        
        result = execute_query(query, params)
        if result:
            flash('Book added successfully!', 'success')
            return redirect(url_for('view_books'))
        else:
            flash('Error adding book!', 'danger')
    
    return render_template('add_book.html')

# Edit book
@app.route('/edit_book/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        genre = request.form.get('genre')
        year = request.form.get('year')
        availability = request.form.get('availability')
        
        query = """UPDATE books SET title=%s, author=%s, genre=%s, year=%s, 
                   availability=%s WHERE book_id=%s"""
        params = (title, author, genre, year, availability, book_id)
        
        execute_query(query, params)
        flash('Book updated successfully!', 'success')
        return redirect(url_for('view_books'))
    
    query = "SELECT * FROM books WHERE book_id = %s"
    book = execute_query(query, (book_id,), fetch=True, fetchone=True)
    return render_template('edit_book.html', book=book)

# Delete book
@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    query = "DELETE FROM books WHERE book_id = %s"
    execute_query(query, (book_id,))
    flash('Book deleted successfully!', 'success')
    return redirect(url_for('view_books'))

# Manage Users
@app.route('/manage_users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not name or not email or not password:
            flash('All fields are required!', 'danger')
            return redirect(url_for('manage_users'))
        
        query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        params = (name, email, password)
        
        result = execute_query(query, params)
        if result:
            flash('User added successfully!', 'success')
        else:
            flash('Error adding user! Email might already exist.', 'danger')
    
    query = "SELECT * FROM users ORDER BY user_id DESC"
    users = execute_query(query, fetch=True)
    return render_template('manage_users.html', users=users)

# Delete user
@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    query = "DELETE FROM users WHERE user_id = %s"
    execute_query(query, (user_id,))
    flash('User deleted successfully!', 'success')
    return redirect(url_for('manage_users'))

# Issue Book
@app.route('/issue_book', methods=['GET', 'POST'])
def issue_book():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        book_id = request.form.get('book_id')
        issue_date = request.form.get('issue_date')
        
        # Check if book is available
        query = "SELECT availability FROM books WHERE book_id = %s"
        book = execute_query(query, (book_id,), fetch=True, fetchone=True)
        
        if book and book['availability'] > 0:
            # Insert issue record
            query = """INSERT INTO issued_books (user_id, book_id, issue_date, status) 
                       VALUES (%s, %s, %s, 'issued')"""
            params = (user_id, book_id, issue_date)
            execute_query(query, params)
            
            # Update book availability
            query = "UPDATE books SET availability = availability - 1 WHERE book_id = %s"
            execute_query(query, (book_id,))
            
            flash('Book issued successfully!', 'success')
            return redirect(url_for('view_issued_books'))
        else:
            flash('Book is not available!', 'danger')
    
    # Fetch users and available books
    users_query = "SELECT * FROM users"
    books_query = "SELECT * FROM books WHERE availability > 0"
    users = execute_query(users_query, fetch=True)
    books = execute_query(books_query, fetch=True)
    
    return render_template('issue_book.html', users=users, books=books)

# View Issued Books
@app.route('/view_issued_books')
def view_issued_books():
    query = """SELECT ib.issue_id, u.name as user_name, b.title as book_title, 
               ib.issue_date, ib.return_date, ib.status
               FROM issued_books ib
               JOIN users u ON ib.user_id = u.user_id
               JOIN books b ON ib.book_id = b.book_id
               ORDER BY ib.issue_id DESC"""
    issued_books = execute_query(query, fetch=True)
    return render_template('view_issued_books.html', issued_books=issued_books)

# Return Book
@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        issue_id = request.form.get('issue_id')
        return_date = request.form.get('return_date')
        
        # Get book_id from issued_books
        query = "SELECT book_id FROM issued_books WHERE issue_id = %s"
        issue = execute_query(query, (issue_id,), fetch=True, fetchone=True)
        
        if issue:
            # Update issued_books record
            query = """UPDATE issued_books SET return_date = %s, status = 'returned' 
                       WHERE issue_id = %s"""
            execute_query(query, (return_date, issue_id))
            
            # Update book availability
            query = "UPDATE books SET availability = availability + 1 WHERE book_id = %s"
            execute_query(query, (issue['book_id'],))
            
            flash('Book returned successfully!', 'success')
            return redirect(url_for('view_issued_books'))
        else:
            flash('Invalid issue ID!', 'danger')
    
    # Fetch issued books that are not returned
    query = """SELECT ib.issue_id, u.name as user_name, b.title as book_title, 
               ib.issue_date
               FROM issued_books ib
               JOIN users u ON ib.user_id = u.user_id
               JOIN books b ON ib.book_id = b.book_id
               WHERE ib.status = 'issued'
               ORDER BY ib.issue_id DESC"""
    issued_books = execute_query(query, fetch=True)
    
    return render_template('return_book.html', issued_books=issued_books)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)