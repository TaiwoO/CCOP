from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Crime (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dispatch = db.Column(db.String(100), unique=False)
    start = db.Column(db.String(100), unique=False)
    street = db.Column(db.String(100), unique=False)
    city = db.Column(db.String(100), unique=False)
    state = db.Column(db.String(100), unique=False)
    zip = db.Column(db.String(100), unique=False)
    crime_class = db.Column(db.String(100), unique=False)
    description = db.Column(db.String(100), unique=False)
    agency = db.Column(db.String(100), unique=False)
    district = db.Column(db.String(100), unique=False)
    latitude = db.Column(db.String(100), unique=False)
    longitude = db.Column(db.String(100), unique=False)

    # def __init__(self):
    #     pass

    def __repr__(self):
        return " Not sure what goes here yet"

    @property
    def serialize(self):
        return{
            'dispatch': self.dispatch,
            'start': self.start,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'zip': self.zip,
            'crime_class': self.crime_class,
            'description': self.description,
            'agency': self.agency,
            'district': self.district,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'agency': self.agency
        }

class Arrest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # def __init__(self):
    #     pass

    def __repr__(self):
        return " Not sure what goes here yet"
