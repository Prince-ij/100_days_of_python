from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, LoginManager, login_user, current_user
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

login_manager = LoginManager()
login_manager.init_app(app)

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "data.sqlite")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', "Gibbrish2xy567849345")
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String)

    todos = db.relationship('Task', back_populates='owner', lazy=True)
    projects = db.relationship('Project', back_populates='owner', lazy=True)

    def __init__(self, email, password):
        self.email = email
        self.password = password


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(32))

    owner = db.relationship('User', back_populates='projects', lazy=True)
    tasks = db.relationship('Task', backref='project', lazy=True)

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(120))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __init__(self, user_id, body, project_id=None):
        self.user_id = user_id
        self.body = body
        self.project_id = project_id

    owner = db.relationship('User', back_populates='todos', lazy=True)

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)




@app.route('/')
def home():

    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['passwd']
        cpasswd = request.form['cpasswd']
        if passwd != cpasswd:
            flash('Passwords do not Match', "error")
            return redirect(url_for('register'))
        user = User.query.filter_by(email=email).first()
        if user:
            flash('User already exists', "error")
            return redirect(url_for('register'))
        else:
            passwd = generate_password_hash(cpasswd)
            user = User(email, passwd)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('signup.html')



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/todo_list')
def create_todo_list():
    pass

@app.route('/delete_todolist/<int:todolist_id>')
def delete_todolist(task_id, todolist_id):
    pass

@app.route('/add_task/<int:todolist_id>')
def add_task(todolist_id):
    pass

@app.route('/delete_task/<int:task_id>/<int:todolist_id>')
def delete_task(task_id, todolist_id):
    pass

@app.route('/modify_task/<int:task_id>/<int:todolist_id>')
def modify_task(task_id, todolist_id):
    pass

@app.route('/dashboard')
def fetch_todo_lists():
    pass

@app.route('/tasks/<int:todolist_id>')
def fetch_tasks(todolist_id):
    pass

if __name__ == '__main__':
    app.run(debug=True)
