# functions for connecting to 3rd party APIs

import requests
import json
from datetime import datetime

# from app import app

from app.models import Crime
from app.models import Arrest

from config import MAPS_API_KEY
from config import GEOCODE_URL
from config import CRIME_URL
from config import ARREST_URL
from config import ENDPOINT_BUFFER_SIZE
from config import OLDEST_CRIME_DATETIME
from config import CRIME_LAST_UPDATED

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
# returns the empty dictionary if geocoding failed
def geocode(street, city, state):
    # replace spaces with plus symbols
    street = street.replace(' ', '+')
    city = city.replace(' ', '+')
    state = state.replace(' ', '+')

    query = GEOCODE_URL + "?address=" + street + ',' + city + ',' + state + "&key=" + MAPS_API_KEY
    data = pulldata(query)

    if(data["results"] == []):
        # sometimes geocoding doesn't work because the address was typed in wrong
        # in this case, put the crime in the middle of the county
        location = {'lng': -77.2405, 'lat': 39.1547}
    else:
        # sloppy, yes, but this is how you get the lat and long with a single line of code
        location = data["results"][0]["geometry"]["location"] if (data != []) else {}
    return location


def getCrime():
    # get info from config
    #API_url = parser.get("crime", "url")
    #from_datetime = parser.get("crime", "last_updated")

    # from_datetime = '2017-01-01T12:00:00.000000'
    from_datetime = CRIME_LAST_UPDATED
    to_datetime = datetime.now().isoformat('T')

    # build the query and pull records from API
    offset = 0
    query = "?$where=start_date > '" + from_datetime + \
        "' and start_date <='" + to_datetime + "'"
    limit = "&$limit=" + str(ENDPOINT_BUFFER_SIZE)
    records = pulldata(CRIME_URL + query + limit)

    clean_data = []

    # page through api records and clean the data
    while(len(records) > 0):
        for record in records:
            dispatch = record["date"]
            start = record["start_date"]
            street = record["location"]
            city = record["city"]
            state = record["state"]
            description = record["narrative"]
            crime_class = record["incident_type"]
            agency = record["agency"]
            district = record["police_district_number"]

            # some of the records don't have geolocations
            if("geolocation" not in record):
                location = geocode(street, city, state)
                latitude = location["lat"]
                longitude = location["lng"]
            else:
                latitude = record["geolocation"]["coordinates"][0]
                longitude = record["geolocation"]["coordinates"][1]
            
            # some zip codes missing, too
            zip = record["zip_code"] if ("zip_code" in record) else 0

            
            this_crime = Crime(dispatch=dispatch, start=start, street=street, city=city, state=state, zip=zip, crime_class=crime_class,
                               description=description, agency=agency, district=district, latitude=latitude, longitude=longitude)
            clean_data.append(this_crime)

        offset += ENDPOINT_BUFFER_SIZE
        records = pulldata(CRIME_URL + query + limit +
                               "&$offset=" + str(offset))

    # update the config 
    CRIME_LAST_UPDATED = to_datetime

    return clean_data
