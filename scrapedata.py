from datetime import datetime

import api_interface as api
from app import app, db, models

# read crimes using api.getCrime
# write the new crimes to the database

def updateCrimes():
    print("{0} crimes added to the database".format(api.getCrime()))
    

if __name__ == "__main__":
    updateCrimes()

    # db_url = "mysql://" + config.get("sql","admin_un") + ':' + config.get("sql","admin_pw") + '@' + config.get("sql","host") + '/' + config.get("sql","db_name")
    # engine = create_engine(db_url, echo=True)

    # schema.Base.metadata.create_all(engine)

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
    # print(output[0])        # output is a list of length 1, so we reference
    # the first element of the list

    # output = api.pulldata(config["arrest_url"] + query)
    # print("\nOne arrest record looks like:")
# print(output[0])
