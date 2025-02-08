from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'


def make_bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper

def make_emphasis(func):
    def wrapper():
        return f'<em>{func()}</em>'
    return wrapper

def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye'


if __name__=='__main__':
    app.run(debug=True)
