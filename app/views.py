# defines web routing for the app
# i.e. which urls display which information

from flask import render_template, jsonify, request
from sqlalchemy import func
from app import app, db
from app.models import Crime, Arrest

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
    min_time = request.args.get('min_time')
    max_time = request.args.get('max_time')

    return jsonify([min_time, max_time])

    # crimes = Crime.query.limit(5).all()
    # return jsonify(crimes=[i.serialize for i in crimes])


# endpoint gives the max and min datetime values in the database
@app.route('/crime/range', methods=['GET'])
def crime_range():
    with app.app_context():
        query_object = db.session.query(func.min(Crime.start))
        min_datetime = str(query_object[0][0])

        # db is empty
        if(min_datetime == 'None'):
            return "crime table is empty"

        query_object = db.session.query(func.max(Crime.start))
        max_datetime = str(query_object[0][0])
    
    return jsonify(min=min_datetime,max=max_datetime)

# endpoint gives the max and min datetime values in the database
@app.route('/arrest/range', methods=['GET'])
def arrest_range():
    with app.app_context():
        query_object = db.session.query(func.min(Arrest.date))
        min_datetime = str(query_object[0][0])

        # db is empty
        if(min_datetime == 'None'):
            return "arrest table is empty"

        query_object = db.session.query(func.max(Arrest.date))
        max_datetime = str(query_object[0][0])
    
    return jsonify(min=min_datetime,max=max_datetime)
