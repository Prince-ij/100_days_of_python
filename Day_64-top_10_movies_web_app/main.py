from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import requests
from config import API_KEY
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

base_dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "movies.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)



class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tmdb_id = db.Column(db.Integer, unique=True)
    title = db.Column(db.String(30), nullable=False, unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String(500))
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(300))
    img_url = db.Column(db.String(300))

    def __repr__(self):
        return f'<Movie {self.title} >'

class EditForm(FlaskForm):
    rating = FloatField('Your Rating out of 10. e.g 7.5', validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddMovie(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating.desc()).all()
    for i, movie in enumerate(movies, start=1):
        movie.ranking = i

    db.session.commit()

    return render_template("index.html", movies=movies)

@app.route('/edit<int:id>', methods=['POST', 'GET'])
def edit(id):
    form = EditForm()
    movie = Movie.query.get(id)
    if form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data

        movie.rating = rating
        movie.review = review

        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit.html', form=form, movie_title=movie.title)


@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        title = form.movie_title.data
        return redirect(url_for('select', title=title))
    return render_template('add.html', form=form)

@app.route('/select/<title>')
def select(title):
    param = {
        'query': title,
        'api_key': API_KEY
    }
    url = 'https://api.themoviedb.org/3/search/movie'

    response = requests.get(url=url, params=param)
    movies = response.json()
    return render_template('select.html', movies=movies['results'])


@app.route('/delete/<int:id>')
def delete(id):
    movie = Movie.query.get(id)

    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/populate/<int:tmdb_id>')
def populate(tmdb_id):
    param = {
        'api_key': API_KEY
    }
    url = f'https://api.themoviedb.org/3/movie/{tmdb_id}'

    response = requests.get(url=url, params=param)
    movie = response.json()

    new_movie = Movie(
        title= movie['original_title'],
        img_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
        year = int(movie['release_date'][:4]),
        description = movie['overview'],
        rating=movie['vote_average'],
        tmdb_id = tmdb_id
    )

    db.session.add(new_movie)
    db.session.commit()



    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
