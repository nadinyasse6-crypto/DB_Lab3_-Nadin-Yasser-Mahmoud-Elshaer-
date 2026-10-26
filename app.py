from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
import pymysql

app = Flask(__name__)
app.secret_key = 'super_secret_key'
bcrypt = Bcrypt(app)

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='WJ28@krhps',
        database='library',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('library'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                           (username, email, hashed_password))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            conn.rollback()
            flash(f'Error: {e}', 'danger')
        finally:
            conn.close()
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            return redirect(url_for('library'))
        else:
            flash('Invalid email or password.', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/library')
def library():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM author")
    authors = cursor.fetchall()
    
    cursor.execute("SELECT * FROM book")
    books = cursor.fetchall()
    
    conn.close()
    return render_template('index.html', authors=authors, books=books, username=session.get('username'))

@app.route('/add_author', methods=['POST'])
def add_author():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    author_id = request.form['author_id']
    name = request.form['name']
    country = request.form['country']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO author (author_id, name, country) VALUES (%s, %s, %s)", 
                       (author_id, name, country))
        conn.commit()
    except Exception as e:
        conn.rollback()
        flash(f'Error: {e}', 'danger')
    finally:
        conn.close()
        
    return redirect(url_for('library'))

@app.route('/edit_author/<int:id>', methods=['GET', 'POST'])
def edit_author(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        try:
            cursor.execute("UPDATE author SET name = %s, country = %s WHERE author_id = %s", (name, country, id))
            conn.commit()
            return redirect(url_for('library'))
        except Exception as e:
            conn.rollback()
            flash(f'Error: {e}', 'danger')
        finally:
            conn.close()
            
    cursor.execute("SELECT * FROM author WHERE author_id = %s", (id,))
    author = cursor.fetchone()
    conn.close()
    return render_template('edit_author.html', author=author)

@app.route('/delete_author/<int:id>')
def delete_author(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM author WHERE author_id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('library'))

@app.route('/add_book', methods=['POST'])
def add_book():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    book_id = request.form['book_id']
    title = request.form['title']
    price = request.form['price']
    author_id = request.form['author_id']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO book (book_id, title, price, author_id) VALUES (%s, %s, %s, %s)", 
                       (book_id, title, price, author_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        flash(f'Error: {e}', 'danger')
    finally:
        conn.close()
        
    return redirect(url_for('library'))

@app.route('/edit_book/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        author_id = request.form['author_id']
        try:
            cursor.execute("UPDATE book SET title = %s, price = %s, author_id = %s WHERE book_id = %s", (title, price, author_id, id))
            conn.commit()
            return redirect(url_for('library'))
        except Exception as e:
            conn.rollback()
            flash(f'Error: {e}', 'danger')
        finally:
            conn.close()
            
    cursor.execute("SELECT * FROM book WHERE book_id = %s", (id,))
    book = cursor.fetchone()
    
    cursor.execute("SELECT * FROM author")
    authors = cursor.fetchall()
    
    conn.close()
    return render_template('edit_book.html', book=book, authors=authors)

@app.route('/delete_book/<int:id>')
def delete_book(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE book_id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('library'))

if __name__ == '__main__':
    app.run(debug=True)