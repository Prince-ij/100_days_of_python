from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'kmkluvsia'

class LoginForm(FlaskForm):
    email    = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[Length(min=8)])
    submit   = SubmitField('Log In')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    email    = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        if email == 'admin@email.com' and password == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
