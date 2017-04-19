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
