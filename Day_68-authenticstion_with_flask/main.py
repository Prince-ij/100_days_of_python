from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__, static_folder='static')
base_url = os.path.abspath(os.path.dirname(__file__))


app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_url, 'users.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()

login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self):
        return f'<User: {self.email}>'


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        password=request.form['password']
        password_hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        if db.session.query(User).filter_by(email=request.form['email']).first():
            flash('Email already registered. Please log in.', 'error')
            return redirect(url_for('login'))
        new_user = User(
            name=request.form['name'],
            email=request.form['email'],
            password=password_hash
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        user = db.session.query(User).filter_by(email=username).first()

        if not user:
            flash('Email not found. Please register.', 'error')
            return redirect(url_for('register'))
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash('Incorrect password. Please try again.', 'error')
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(app.static_folder,'files/cheat_sheet.pdf' )

if __name__ == "__main__":
    app.run(debug=True)
