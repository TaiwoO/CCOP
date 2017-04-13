from flask import render_template, jsonify, request
from app import app
from app.models import Crime

# The home route
@app.route('/')
@app.route('/index')
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
