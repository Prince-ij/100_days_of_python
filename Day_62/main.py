from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe       = StringField('Cafe name', validators=[DataRequired()])
    location   = StringField('Cafe Location on Google Maps(URL)', validators=[DataRequired(), URL()])
    open_time  = StringField('Opening time e.g 8AM', validators=[DataRequired()])
    close_time = StringField('Closing time e.g 5:30PM', validators=[DataRequired()])
    wifi_r     = SelectField('Wifi Strenght Rating', choices=['💪' * i for i in range(6)] + ['✘'],
                             validators=[DataRequired()], default='✘')
    coffee_r   = SelectField('Coffee Rating', choices=['☕' * i for i in range(6)] + ['✘'],
                             validators=[DataRequired()], default='✘')
    outlet_r   = SelectField('Power Socket Availability', choices=['🔌' * i for i in range(6)] + ['✘'],
                             validators=[DataRequired()], default='✘')
    submit     = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_row = f'{form.cafe.data}, {form.location.data}, {form.open_time.data}, {form.close_time.data},{form.coffee_r.data}, {form.wifi_r.data}, {form.outlet_r.data}\n'
        with open(os.path.join(os.path.dirname(__file__), 'cafe-data.csv'), newline='', encoding='utf-8', mode='a') as f:
            f.write(new_row)
            return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open(os.path.join(os.path.dirname(__file__), 'cafe-data.csv'), newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
