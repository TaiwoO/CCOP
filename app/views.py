# defines web routing for the app
# i.e. which urls display which information

from flask import render_template, jsonify, request
from app import app
from app.models import Crime

# The home route (homepage)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# crime endpoint
# URL query format has not yet been defined
# likely we'll need filtering on time, lat/long, and crime types
# potentially have a field for limiting the number of records
@app.route('/crime', methods=['GET'])
def crimes():
    crimes = Crime.query.all()
    return jsonify(crimes=[i.serialize for i in crimes])


# probably unnecessary
'''
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
'''
