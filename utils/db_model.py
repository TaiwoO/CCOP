from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Crime (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address_number = db.Column(db.String(100), unique=False)
    agency = db.Column(db.String(100), unique=False)
    beat = db.Column(db.String(100), unique=False)
    case_number = db.Column(db.String(100), unique=False)
    city = db.Column(db.String(100), unique=False)
    date = db.Column(db.String(23), unique=False)
    district = db.Column(db.String(100), unique=False)
   # end_date = db.Column(db.String(23), unique=False) # some dont have
   # end_date
    longitude = db.Column(db.Float, unique=False)
    latitude = db.Column(db.Float, unique=False)
    geolocation_address = db.Column(db.String(100), unique=False)
    geolocation_city = db.Column(db.String(100), unique=False)
    geolocation_state = db.Column(db.String(100), unique=False)
    geolocation_zip = db.Column(db.String(100), unique=False)
    incident_id = db.Column(db.String(100), unique=False)
    incident_type = db.Column(db.String(100), unique=False)
    location = db.Column(db.String(100), unique=False)
    narrative = db.Column(db.String(100), unique=False)
    place = db.Column(db.String(100), unique=False)
    police_district_number = db.Column(db.String(100), unique=False)
    pra = db.Column(db.String(100), unique=False)
    sector = db.Column(db.String(100), unique=False)
    start_date = db.Column(db.String(23), unique=False)
    state = db.Column(db.String(100), unique=False)
    zip_code = db.Column(db.Integer, unique=False)

    # def __init__(self):
    #     pass

    def __repr__(self):
        return " Not sure what goes here yet"

    @property
    def serialize(self):
        return{
            'address_number': self.address_number,
            'agency': self.agency,
            'beat': self.beat,
            'case_number': self.case_number,
            'city': self.city,
            'date': self.date,
            'district': self.district,
            # end_date = db.Column(db.String(23), unique=False) # some dont
            # have end_date
            'longitude': self.longitude,
            'latitude': self.latitude,
            'geolocation_address': self.geolocation_address,
            'geolocation_city': self.geolocation_city,
            'geolocation_state': self.geolocation_state,
            'geolocation_zip': self.geolocation_zip,
            'incident_id': self.incident_id,
            'incident_type': self.incident_type,
            'location': self.location,
            'narrative': self.narrative,
            'place': self.place,
            'police_district_number': self.police_district_number,
            'pra': self.pra,
            'sector': self.sector,
            'start_date': self.start_date,
            'state': self.state,
            'zip_code': self. zip_code
        }


class Arrest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # def __init__(self):
    #     pass

    def __repr__(self):
        return " Not sure what goes here yet"
