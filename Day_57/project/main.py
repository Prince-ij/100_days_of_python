from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    posts = requests.get(blog_url).json()
    return render_template('index.html', posts=posts)

@app.route('/read/<int:id>')
def read(id):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    posts = requests.get(blog_url).json()
    for post in posts:
        if post['id'] == id:
            return render_template('post.html', post=post)
    return "Post not found", 404

if __name__ == "__main__":
    app.run(debug=True)
