# TaskLight - Simple Task Manager

A beautiful, responsive task management web application built with Flask and Bootstrap.

## Features

- Create and manage projects
- Add tasks to projects or as standalone items
- User authentication (login/register)
- Responsive design for all devices
- Modern Bootstrap 5 interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Prince-ij/100_days_of_python.git
   cd 100_days_of_python/day_88_task_manager_web_app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python3 main.py
   ```

4. Open your browser and go to `http://localhost:5000`

## Usage

1. Create an account or login
2. Create projects to organize your tasks
3. Add tasks to projects or create quick standalone tasks
4. View and manage all your projects from the dashboard

## Project Structure

```
├── main.py                    # Main Flask application
├── templates/                 # HTML templates
├── static/                    # CSS and static files
├── data.sqlite               # SQLite database (auto-generated)
└── requirements.txt           # Python dependencies
```

## Dependencies

- Flask - Web framework
- Flask-SQLAlchemy - Database ORM
- Flask-Login - User session management
- Werkzeug - Password hashing
- Bootstrap 5 - Frontend framework

## License

MIT License
