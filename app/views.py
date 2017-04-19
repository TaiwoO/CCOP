# defines web routing for the app
# i.e. which urls display which information

from datetime import datetime

from flask import render_template, jsonify, request
from sqlalchemy import func

from app import app, db
from app.models import Crime, Arrest

from config import JS_DATETIME_PARSE_STRING
from config import MAX_CRIMES
from config import MAX_ARRESTS

# The home route (homepage)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# crime endpoint
'''
sample url:
http://localhost:5000/crime?min_time=2017-04-01T15:47:13.657Z&max_time=2017-04-19T15:47:13.657Z&bounds=38.955865,-77.232668,39.1646,-77.055342

url query args:
datetimes are the javascript Date.toJSON() format
min_time=2017-04-01T15:47:13.657Z
max_time=2017-04-19T15:47:13.657Z

lat/long query args:
uses google.maps.Map.getBounds().toUrlValue() format,
that is: lat_lo,lng_lo,lat_hi,lng_hi
bounds=38.955865,-77.232668,39.1646,-77.055342
'''
# potentially have a field for limiting the number of records
@app.route('/crime', methods=['GET'])
def crimes():
    # parse time slider values
    min_time = datetime.strptime(request.args.get('min_time'),JS_DATETIME_PARSE_STRING)
    max_time = datetime.strptime(request.args.get('max_time'),JS_DATETIME_PARSE_STRING)

    # parse map boundary values
    bounds = [float(i) for i in request.args.get('bounds').split(',')]

    # query the db
    crimes = Crime.query.filter(Crime.start >= min_time) \
                        .filter(Crime.start <= max_time) \
                        .filter(Crime.latitude > bounds[0]) \
                        .filter(Crime.latitude < bounds[2]) \
                        .filter(Crime.longitude > bounds[1]) \
                        .filter(Crime.longitude < bounds[3]) \
                        .limit(MAX_CRIMES).all()
    return jsonify(crimes=[i.serialize for i in crimes])


# endpoint gives the max and min datetime values in the database
# this is for both crime and arrest data
@app.route('/range', methods=['GET'])
def range():
    with app.app_context():
        minCrime = db.session.query(func.min(Crime.start))[0][0]
        minArrest = db.session.query(func.min(Arrest.date))[0][0]

        if(minCrime == None and minArrest == None):
            return "the database is empty"
        
        maxCrime = db.session.query(func.max(Crime.start))[0][0]
        maxArrest = db.session.query(func.max(Arrest.date))[0][0]

        min_datetime = str(min(minCrime, minArrest))
        max_datetime = str(max(maxCrime, maxArrest))
    
    return jsonify(min=min_datetime,max=max_datetime)
