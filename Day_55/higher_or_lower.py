from flask import Flask
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return '''<h1>Guess a number from between 1 to 9</h1>
            <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="300">'''

@app.route('/<int:num>')
def guessed(num):
    guess = randint(1, 9)
    if num == guess:
        return '''<h2>Correct!</h2>
                <iframe src="https://giphy.com/embed/uVpPvvpU3nip5pBkPD" width="480" height="264" style="" frameBorder="0" class="giphy-embed" allowFullScreen>
                    </iframe><p><a href="">via GIPHY</a></p>'''
    if num < guess:
        return '''<h2>Too Low!</h2>
                        <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXBmejdqZHA2NHJlNTdxdGczcW11aGQwbDg0Ym5uMDJzMTZzeWcyaSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/qBHeRGQKKsacqmCQqP/giphy.gif" width="300">'''

    if num > guess:
        return '''<h2>Too high!</h2>
                <img src="https://media.giphy.com/media/YKroe55zFMIwpmBCu6/giphy.gif?cid=790b7611agwg9xjks4f8pk56ocusejwyu42qlfyp5lu4eu0d&ep=v1_gifs_search&rid=giphy.gif&ct=g" width="300">'''

if __name__=='__main__':
    app.run()
