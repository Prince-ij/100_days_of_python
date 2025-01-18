from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
import os
base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(base_dir, 'cafes.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route('/random')
def random():
    cafe = db.session.query(Cafe).all()
    if not cafe:
        return jsonify(error="No cafes found"), 404
    random_cafe = choice(cafe)
    return jsonify(cafe=random_cafe.to_dict())

@app.route('/all')
def all():
    cafes = db.session.query(Cafe).all()
    all_cafes = []
    for cafe in cafes:
        all_cafes.append(cafe.to_dict())

    return jsonify(cafes=all_cafes)

@app.route('/search')
def search():
    location = request.args.get('location')
    if location:
        place = location.title()
        cafes = db.session.query(Cafe).filter_by(location=place).all()
        return jsonify(cafe=[found.to_dict() for found in cafes])
    else:
        return jsonify(error="Location parameter is missing"), 400

## HTTP POST - Create Record

@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('has_toilet')),
        has_wifi=bool(request.form.get('has_wifi')),
        has_sockets=bool(request.form.get('has_sockets')),
        can_take_calls=bool(request.form.get('can_take_calls')),
        coffee_price=request.form.get('coffee_price')
        )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Cafe added successfully"})

## HTTP PUT/PATCH - Update Record

@app.route('/update_price/<int:id>', methods=['PATCH'])
def update_price(id):
    cafe = db.session.query(Cafe).get(id)
    new_price = request.args.get('new_price')

    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={'Success': 'Cafe price updated successfully'})

    else:
        return jsonify(error={'Error': 'id not found in database'}), 404


## HTTP DELETE - Delete Record

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    cafe = db.session.query(Cafe).get(id)
    api_key = request.args.get('api_key')

    if cafe:
        if api_key == 'TopSecretApiKey':
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={'Success': 'Cafe has been successfully erased'})
        else:
            return jsonify(error={'Sorry': 'wrong api key'}), 403
    else:
        return jsonify(error={'Error': 'id not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
