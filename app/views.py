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
from config import CRIME_TYPES

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

# arrest endpoint
'''
sample url:
http://localhost:5000/arrest?min_time=2017-04-01T15:47:13.657Z&max_time=2017-04-19T15:47:13.657Z&bounds=38.955865,-77.232668,39.1646,-77.055342

url query args:
datetimes are the javascript Date.toJSON() format
min_time=2017-04-01T15:47:13.657Z
max_time=2017-04-19T15:47:13.657Z

lat/long query args:
uses google.maps.Map.getBounds().toUrlValue() format,
that is: lat_lo,lng_lo,lat_hi,lng_hi
bounds=38.955865,-77.232668,39.1646,-77.055342
'''
@app.route('/arrest', methods=['GET'])
def arrests():
    # parse time slider values
    min_time = datetime.strptime(request.args.get('min_time'),JS_DATETIME_PARSE_STRING)
    max_time = datetime.strptime(request.args.get('max_time'),JS_DATETIME_PARSE_STRING)

    # parse map boundary values
    bounds = [float(i) for i in request.args.get('bounds').split(',')]

    # query the db
    arrests = Arrest.query.filter(Arrest.date >= min_time) \
                        .filter(Arrest.date <= max_time) \
                        .filter(Arrest.latitude > bounds[0]) \
                        .filter(Arrest.latitude < bounds[2]) \
                        .filter(Arrest.longitude > bounds[1]) \
                        .filter(Arrest.longitude < bounds[3]) \
                        .limit(MAX_ARRESTS).all()
    return jsonify(arrests=[i.serialize for i in arrests])


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

# endpoint gives the categories of crime and their respective frequencies
# TODO: adjust query result based on the map boundaries and time slider much like the crime endpoint
@app.route('/crime/type', methods=['GET'])
def crime_type():
    noArgs = True
    if(request.args.get('min_time') is not None):
        noArgs = False
        # parse time slider values
        min_time = datetime.strptime(request.args.get('min_time'),JS_DATETIME_PARSE_STRING)
        max_time = datetime.strptime(request.args.get('max_time'),JS_DATETIME_PARSE_STRING)

        # parse map boundary values
        bounds = [float(i) for i in request.args.get('bounds').split(',')]

    crime_types = {crime_type:0 for crime_type in CRIME_TYPES}  # Blank Normalized categories 
    
    # Use all of our Nomalized crime type categories to match with the API's crime description
    # Example: 'Assult': ["AGG", "ASSAULT"]
    # "Assult" is a Normalized crime type and ["AGG", "ASSAULT"] are the prefixes for that crime type
    if(noArgs):
        not_categorized = Crime.query.count()
    else:
        not_categorized = Crime.query.filter(Crime.start >= min_time) \
                                           .filter(Crime.start <= max_time) \
                                           .filter(Crime.latitude > bounds[0]) \
                                           .filter(Crime.latitude < bounds[2]) \
                                           .filter(Crime.longitude > bounds[1]) \
                                           .filter(Crime.longitude < bounds[3]) \
                                           .count();
    for crime_type, crime_prefixes in CRIME_TYPES.items():
        # Get the total number of matches for a crime_type based on the prefixes
        for prefix in crime_prefixes:
            if(not noArgs):
                total_matches = Crime.query.filter(Crime.start >= min_time) \
                                           .filter(Crime.start <= max_time) \
                                           .filter(Crime.latitude > bounds[0]) \
                                           .filter(Crime.latitude < bounds[2]) \
                                           .filter(Crime.longitude > bounds[1]) \
                                           .filter(Crime.longitude < bounds[3]) \
                                           .filter(Crime.description.like("%"+prefix+"%")) \
                                           .count()
            else:
                total_matches = Crime.query.filter(Crime.description.like("%"+prefix+"%")).count()
            crime_types[crime_type] += total_matches
            not_categorized -= total_matches
    crime_types['Other'] = not_categorized

    return jsonify(crime_types = crime_types)
