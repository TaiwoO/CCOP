# CURRENTLY:
# 	reads the config file
#	pulls the most recent data from the endpoints
# PLANNED:
#	stores the data in the database

import sys
sys.path.insert(0, "../")	# allow importing code from src

# from ConfigParser import SafeConfigParser
# import MySQLdb
from datetime import datetime
from sqlalchemy import create_engine

import api_interface as api
import config_interface as cfg
from ..db import schema

# engine used for connecting to the database

# returns a connection to a database
# TODO: add exception handling?
# def db_connect(username, password, database="ccop", host="localhost"):
#	db = MySQLdb.connect(user=username, passwd=password, db=database, host=host)
#	return db

# read crimes using api.getCrime
# write the new crimes to the database
def updateCrimes(parser):
	# read necessary data from the parser
	sql_username = parser.get("sql","super_user")
	sql_password = parser.get("sql","super_pw")

	# connect to the database
	db_connection = db_connect(sql_username, sql_password)
	db_cursor = db_connection.cursor()

	# build the query and pull records from API
	offset = 0
	query = "?$where=start_date > '" + from_datetime + "' and start_date <='" + to_datetime + "'"
	limit = "&$limit=" + str(api.BUFFER_SIZE)
	records = api.pulldata(API_url + query + limit)

	total_read = 0;
	# parse the records and insert into database
	while(len(records) > 0):
		for record in records:
			dispatch = record["date"]
			start = record["start_date"]
			street = record["location"]
			city = record["city"]
			state = record["state"]

			# some of the records don't have geolocations
			if("geolocation" not in record):
				location = api.geocode(street, city, state, config["geocode_url"], config["google_key"])
				latitude = location["lat"]
				longitude = location["lng"]
			else:
				latitude = record["geolocation"]["coordinates"][0]
				longitude = record["geolocation"]["coordinates"][1]

			# some zip codes missing, too
			if("zip_code" in record):
				zip = record["zip_code"]
			else:
				zip = 0

			crime_class = record["incident_type"]
			agency = record["agency"]
			district = record["police_district_number"]

			db_cursor.execute("""INSERT INTO crimes (dispatch, start, latitude, longitude, street, city, state, zip, class, agency, district)
					     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
					     (dispatch, start, latitude, longitude, street, city, state, zip, crime_class, agency, district))

		total_read += len(records)	# keep track of records read

		# read the next 500 records
		offset += api.BUFFER_SIZE
		records = api.pulldata(API_url + query + limit + "&$offset=" + str(offset))


	# commit the insertions to the db
	db_connection.commit()
	db_cursor.close()	# very important!
	return total_read

if __name__ == "__main__":
	config = cfg.readConfig()
    
	db_url = "mysql://" + config.get("sql","admin_un") + ':' + config.get("sql","admin_pw") + '@' + config.get("sql","host") + '/' + config.get("sql","db_name")
	engine = create_engine(db_url, echo=True)
	
	schema.Base.metadata.create_all(engine)
    
	# r = updateCrimes(db, config["crime_url"], '2017-02-01T00:00:00.000')
	# print("%d new crime records were found and stored" % r)

	# example of how to call the geocoding function
	# also shows how to get info from the dictionary of config file data
	# location = api.geocode("1000 Hilltop Circle","Baltimore","MD", config["geocode_url"], config["google_key"])
	# print("\nUMBC's location is at latitude:" + str(location['lat']) + " and longitude:" + str(location['lng']))

	# sample for paging through data from the crime and arrest APIs
	# will give you a number of records = limit, starting at the offset
	# query = "?$limit=1&$offset=0"


	# note: Python 2.7 prints a leading 'u' on most of the data because it's unicode
	# formatted and the default for Python 2.7 is ASCII encoding.  This affects readability,
	# but not functionality unless you do some crazy string conversions
	# output = api.pulldata(config["crime_url"] + query)
	# print("\nOne crime record looks like:")
	# print(output[0])	# output is a list of length 1, so we reference the first element of the list

	# output = api.pulldata(config["arrest_url"] + query)
        # print("\nOne arrest record looks like:")
	#print(output[0])
