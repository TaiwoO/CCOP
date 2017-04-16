# functions for connecting to 3rd party APIs

import requests
import json
from datetime import datetime

from app import app, db
from app.models import Crime
from app.models import Arrest
from exceptions import RequestLimitReachedError
from exceptions import PartialDataError

from config import MAPS_API_KEY
from config import GEOCODE_URL
from config import CRIME_URL
from config import ARREST_URL
from config import ENDPOINT_BUFFER_SIZE
from config import OLDEST_CRIME_DATETIME
from config import OLDEST_ARREST_DATETIME
from config import SQLALCHEMY_DATABASE_URI
from config import CRIME_DATETIME_PARSE_STRING
from config import ARREST_DATETIME_PARSE_STRING

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

# runs a get request at the provided url
# returns the json from the API if the request succeeds
# otherwise returns an empty list
def pulldata(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

# takes in a street address, city, and state
# returns a dictionary containing the latitude and longitude of the address
# returns the center of MoCo if the street address cannot be resolved or if connecting to the geocoding API fails
# raises RequestLimitReachedError if api requests have been exhausted
def geocode(street, city, state):
    # replace spaces with plus symbols
    street = street.replace(' ', '+') if (street is not None) else ""
    city = city.replace(' ', '+') if (city is not None) else ""
    state = state.replace(' ', '+') if (state is not None) else ""

    query = GEOCODE_URL + "?address=" + street + ',' + city + ',' + state + "&key=" + MAPS_API_KEY
    data = pulldata(query)

    query_status = data["status"]
    
    if(query_status == "OK"):
        # sloppy, yes, but this is how you get the lat and long with a single line of code
        location = data["results"][0]["geometry"]["location"]
    elif(query_status == "ZERO_RESULTS"):
        # sometimes geocoding doesn't work because the address was typed in wrong
        # in this case, put the crime in the middle of the county
        location = {'lat': -77.2405, 'lng': 39.1547}
    elif(query_status == "OVER_QUERY_LIMIT"):
        raise RequestLimitReachedError()
    else:
        # handle other error types by geocoding to default location
        location = {'lat': -77.2405, 'lng': 39.1547}

    return location

# takes either the Crime or Arrest model as input
# returns a datetime string of the most recent record listed in the db
def readMostRecentRecord(model):
    with app.app_context():
        if(model == Crime):
            # this returns a sqlalchemy query object
            query_object = db.session.query(func.max(Crime.dispatch))
        elif(model == Arrest):
            # TODO make sure the Arrest.date field matches the Arrest model
            query_object = db.session.query(func.max(Arrest.date))
        else:
            return "don't do that"
    
    most_recent_time = str(query_object[0][0])
    # db is empty
    if(most_recent_time == 'None'):
        if(model == Crime):
            most_recent_time = OLDEST_CRIME_DATETIME
        elif(model == Arrest):
            most_recent_time = OLDEST_ARREST_DATETIME
        else:
            return "don't do that"
    return most_recent_time
    
def getCrime():
    from_datetime = readMostRecentRecord(Crime)
    to_datetime = datetime.now().isoformat('T')

    # build the query and pull records from API
    offset = 0
    query = "?$where=start_date > '" + from_datetime + \
        "' and start_date <='" + to_datetime + "'"
    limit = "&$limit=" + str(ENDPOINT_BUFFER_SIZE)
    order = "&$order=start_date"
    records = pulldata(CRIME_URL + query + order + limit)

    totalCrimes = 0
    # page through api records and clean the data
    while(len(records) > 0):
        clean_data = []
        for record in records:
            dispatch = datetime.strptime(record["date"],CRIME_DATETIME_PARSE_STRING) if ("date" in record) else None
            start = datetime.strptime(record["start_date"],CRIME_DATETIME_PARSE_STRING) if ("start_date" in record) else None
            street = record["location"] if ("location" in record) else None
            city = record["city"] if ("city" in record) else None
            state = record["state"] if ("state" in record) else None
            description = record["narrative"] if ("narrative" in record) else None
            crime_class = record["incident_type"] if ("incident_type" in record) else None
            agency = record["agency"] if ("agency" in record) else None
            district = record["police_district_number"] if ("police_district_number" in record) else None

            if("geolocation" in record and "latitude" in record["geolocation"] and "longitude" in record["geolocation"]):
                # latitude and longitude are provided
                latitude = record["geolocation"]["latitude"]
                longitude = record["geolocation"]["longitude"]
                
            # record missing lat/long info
            else:
                try:
                    location = geocode(street, city, state)
                    latitude = location["lat"]
                    longitude = location["lng"]
                except RequestLimitReachedError:
                    raise PartialDataError(totalCrimes, "crime")
            
            # some zip codes missing, too
            zip = record["zip_code"] if ("zip_code" in record) else 0

            this_crime = Crime(dispatch=dispatch, start=start, street=street, city=city, state=state, zip=zip, crime_class=crime_class,
                               description=description, agency=agency, district=district, latitude=latitude, longitude=longitude)
            clean_data.append(this_crime)
        
        # write clean data to database
        with app.app_context():
            for crime in clean_data:
                db.session.add(crime)
            db.session.commit()
        totalCrimes += len(clean_data)

        offset += ENDPOINT_BUFFER_SIZE
        records = pulldata(CRIME_URL + query + order + limit + "&$offset=" + str(offset))

    return totalCrimes


def getArrest():
    from_datetime = readMostRecentRecord(Arrest)
    to_datetime = datetime.now().isoformat('T')

    # build the query and pull records from API
    offset = 0
    query = "?$where=arrest_date > '" + from_datetime + \
        "' and arrest_date <='" + to_datetime + "'"
    limit = "&$limit=" + str(ENDPOINT_BUFFER_SIZE)
    order = "&$order=arrest_date"
    records = pulldata(ARREST_URL + query + order + limit)
    
    totalArrests = 0
    # page through api records and clean the data
    while(len(records) > 0):
        clean_data = []
        for record in records:
            date = datetime.strptime(record["arrest_date"],ARREST_DATETIME_PARSE_STRING)
            street = record["street"] if ("street" in record) else None
            city = record["city"] if ("city" in record) else None
            state = record["state"] if ("state" in record) else None
            offense = record["offense"] if ("offense" in record) else None
            first = record["first_name"] if ("first_name" in record) else None
            last = record["last_name"] if ("last_name" in record) else None
            
            try:
                location = geocode(street, city, state)
            except RequestLimitReachedError as err:
                print(err.message)
                raise PartialDataError(totalArrests, "arrest")
            latitude = location["lat"]
            longitude = location["lng"]

            if("middle_name" not in record):
                middle = None
            else:
                middle = record["middle_name"]

            this_arrest = Arrest(date=date, street=street, city=city, state=state, offense=offense, first=first, middle=middle, last=last, latitude=latitude, longitude=longitude)
            clean_data.append(this_arrest) 
        
        # write clean data to database
        with app.app_context():
            for arrest in clean_data:
                db.session.add(arrest)
            db.session.commit()
        totalArrests += len(clean_data)

        offset += ENDPOINT_BUFFER_SIZE
        records = pulldata(CRIME_URL + query + order + limit + "&$offset=" + str(offset))

    return totalArrests

if __name__ == "__main__":
    try:
        print("Fetching new arrest data. This operation WILL take a while...")
        print("{0} crimes added to the database".format(getArrest()))
        print("Fetching new crime data. This operation may take a while...")
        print("{0} crimes added to the database".format(getCrime()))
    except PartialDataError as err:
        print(err.message)
        print("now quitting...")
