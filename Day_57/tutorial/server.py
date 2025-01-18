from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template('index.html', num=random_number, year=year)

@app.route('/<name>')
def guess_age(name):
    param = {
        'name': name
    }
    gender = requests.get('https://api.genderize.io', params=param).json()['gender']
    age = requests.get('https://api.agify.io/', params=param).json()['age']
    return render_template('agify.html', gender=gender, age=age, name=name)

@app.route('/blogs')
def blog():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    posts = requests.get(blog_url).json()
    return render_template('blog.html', posts=posts)

if __name__ == '__main__':
    app.run()
