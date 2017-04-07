import sys
sys.path.insert(0, 'utils')

from flask import Flask, jsonify, render_template
from db_model import db, Crime, Arrest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDB.db'
db.init_app(app)

# The home route


@app.route('/')
def index():
    return render_template('index.html')

# Crimes


@app.route('/crime', methods=['GET'])
def crimes():
    crimes = Crime.query.all()
    return jsonify(crimes=[i.serialize for i in crimes])

# Crime by case_number


@app.route('/crime/case/<case_number>', methods=['GET'])
def crime_by_case(case_number):
    crime = Crime.query.filter_by(case_number=case_number).one()
    return jsonify(crime.serialize)

# Crime(s) by city


@app.route('/crime/city/<city>', methods=['GET'])
def crime_by_city(city):
    crimes = Crime.query.filter_by(city=city).all()
    return jsonify(crimes=[i.serialize for i in crimes])


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
