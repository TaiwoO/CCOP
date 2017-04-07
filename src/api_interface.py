# functions for connecting to 3rd party APIs

import sys
sys.path.insert(0, "../")	# allow importing code from other directories under src

import requests
import json
from datetime import datetime

# stuff from /src
import config_interface as cfg
from ..db import schema

# global "constants"
BUFFER_SIZE = 500

# runs a get request at the provided url
# returns the json from the API if the request succeeds
# otherwise returns an empty list
def pulldata(url):
	response = requests.get(url)
	if response.status_code == 200:
		return response.json()
	return []

# takes in a ConfigParser, street address, city, and state
# returns a dictionary containing the latitude and longitude of the address
# returns the empty dictionary if geocoding failed
def geocode(parser, street, city, state):
    # get info from config
	url = parser.read("google_api","geocode_url")
	API_key = parser.read("google_api","api_key")
    
	# replace spaces with plus symbols
	street = street.replace(' ', '+')
	city = city.replace(' ', '+')
	state = state.replace(' ', '+')

	query = url + "?address=" + street + ',' + city + ',' + state + "&key=" + API_key
	data = pulldata(query)
	# sloppy, yes, but this is how you get the lat and long with a single line of code
	location = data["results"][0]["geometry"]["location"] if (data != []) else {}
	return location

def getCrime(parser):
	# get info from config
	API_url = parser.get("crime","url")
	from_datetime = parser.get("crime","last_updated")
	to_datetime=datetime.now().isoformat('T')

	# build the query and pull records from API
	offset = 0
	query = "?$where=start_date > '" + from_datetime + "' and start_date <='" + to_datetime + "'"
	limit = "&$limit=" + str(BUFFER_SIZE)
	records = pulldata(API_url + query + limit)
	
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
				location = geocode(parser, street, city, state)
				latitude = location["lat"]
				longitude = location["lng"]
			else:
				latitude = record["geolocation"]["coordinates"][0]
				longitude = record["geolocation"]["coordinates"][1]

			# some zip codes missing, too
			zip = record["zip_code"] if ("zip_code" in record) else 0
			
			this_crime = Crime(dispatch=dispatch, start=start, street=street, city=city, state=state, zip=zip, crime_class=crime_class, description=description, agency=agency, district=district, latitude=latitude, longitude=longitude)
			clean_data.append(this_crime)
		
		offset += BUFFER_SIZE
		records = api.pulldata(API_url + query + limit + "&$offset=" + str(offset))
		
	# update the config file
	parser.set("crime","last_updated",to_datetime)
	cfg.writeConfig(parser)
	
	return clean_data
	


