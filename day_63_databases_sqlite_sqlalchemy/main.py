from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "new-books-collection.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# db  = sqlite3.connect('books-collection.db')

# all_books = []
# cursor    = db.cursor()

# cursor.execute('CREATE TABLE books(id INTEGER PRIMARY KEY, title VARCHAR(250) NOT NULL UNIQUE,\
#                 author VARCHAR(250) NOT NULL, rating FLOAT NOT NULL)')

# cursor.execute('INSERT INTO books VALUES(2, "Barbarosa", "Hyreddin", "5.7")')
# db.commit()


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True)
    author = db.Column(db.String(20), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
       return f'< Book: {self.title} >'

# new_book = Books(id=1, title='Harry Potter', author='JK. Rowlings', rating=9.3)
# with app.app_context():
#     db.session.add(new_book)
#     db.session.commit()

@app.route('/')
def home():
    books = Books.query.all()
    return render_template('index.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name   = request.form.get('name')
        author = request.form.get('author')
        rating = request.form.get('rating')

        # new_dict = {
        #     'title': name,
        #     'author': author,
        #     'rating': rating
        # }

        # all_books.append(new_dict)
        new_user = Books(title=name, author=author, rating=rating)
        db.session.add(new_user)
        db.session.commit()
    return render_template('add.html')



@app.route('/edit/<int:id>', methods=['POST', 'GET'])
def edit(id):
    book = Books.query.get(id)
    return render_template('edit_rating.html', book=book)

@app.route('/edited/<int:id>', methods=['POST', 'GET'])
def edited(id):
    book = Books.query.get(id)
    if request.method == 'POST':
        book.rating = float(request.form.get('rating'))
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>')
def delete(id):
    book = Books.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
