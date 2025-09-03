from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin, LoginManager, login_user, current_user, logout_user, login_required
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

    tasks = db.relationship('Task', back_populates='owner', lazy=True)
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

    owner = db.relationship('User', back_populates='tasks', lazy=True)

with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user




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



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        passwd = request.form.get('passwd')

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('User not Found', "error")
            return redirect(url_for('login'))

        if not check_password_hash(user.password, passwd):
            flash('Wrong Password buddy, Try again', "error")
            return redirect(url_for('login'))

        login_user(user)
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user_projects = current_user.projects
    user_tasks = current_user.tasks
    return render_template('dashboard.html', projects=user_projects, tasks=user_tasks, user=current_user)

@app.route('/create_project/<int:user_id>',  methods=['GET', 'POST'])
def create_project(user_id):
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            project = Project(user_id, name)
            db.session.add(project)
            db.session.commit()
            flash(f'Project {name} Created Successfully', "success")
            return redirect(url_for('dashboard'))
        else:
            flash('Error: Project name must be set', "error")
            return redirect(url_for('dashboard'))

@app.route('/create_task/<int:user_id>', methods=['GET', 'POST'])
def create_task(user_id):
    if request.method == 'POST':
        body = request.form.get('body')
        if body:
            task = Task(user_id, body)
            db.session.add(task)
            db.session.commit()
            flash(f'Task Created Successfully', "success")
            return redirect(url_for('dashboard'))
        else:
            flash('Error: Task must be specified', "error")
            return redirect(url_for('dashboard'))

@app.route('/delete_task/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task has been Deleted Successfully', 'success')
    return redirect(url_for('dashboard'))

@app.route('/delete_project/<int:project_id>', methods=['GET', 'POST'])
def delete_project(project_id):
    project = Project.query.get(project_id)
    tasks = project.tasks
    db.session.delete(project)
    for task in tasks:
        db.session.delete(task)
    db.session.commit()
    flash('Project has been Deleted Successfully', 'success')
    return redirect(url_for('dashboard'))

@app.route('/add_project_task/<int:user_id>/<int:project_id>', methods=['GET', 'POST'])
def add_project_task(user_id, project_id):
    if request.method == 'POST':
        body = request.form.get('body')
        if body:
            task = Task(user_id, body, project_id)
            db.session.add(task)
            db.session.commit()
            flash(f'Task Created Successfully', "success")
            return redirect(url_for('dashboard'))
        else:
            flash('Error: Task must be specified', "error")
            return redirect(url_for('dashboard'))
    user = User.query.get(user_id)
    project = Project.query.filter_by(id=project_id).filter_by(user_id=current_user.id).first()
    return render_template('add_project_task.html', user=user, project=project)

@app.route('/delete_project_task/<int:task_id>/<int:project_id>', methods=['GET', 'POST'])
def delete_project_task(project_id, task_id):
    task = Task.query.filter_by(project_id=project_id).filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    flash(f'Task deleted Successfully', "success")
    return redirect(url_for('dashboard'))

@app.route('/project_view/<int:project_id>')
def project_view(project_id):
    project = Project.query.filter_by(id=project_id).filter_by(user_id=current_user.id).first()
    return render_template('open_project.html', user=current_user, project=project)

@app.route('/add_project_task_view/<int:project_id>')
def view_add(project_id):
    project = Project.query.filter_by(id=project_id).filter_by(user_id=current_user.id).first()
    user = User.query.get(current_user.id)
    return render_template('add_project_task.html', project=project, user=user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
