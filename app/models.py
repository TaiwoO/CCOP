from app import db

class Crime (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dispatch = db.Column(db.DateTime, unique=False)
    start = db.Column(db.DateTime, index=True, unique=False)
    street = db.Column(db.String(70), unique=False)
    city = db.Column(db.String(50), unique=False)
    state = db.Column(db.String(2), unique=False)
    zip = db.Column(db.String(10), unique=False)
    crime_class = db.Column(db.String(10), index=True, unique=False)
    description = db.Column(db.String(100), unique=False)
    agency = db.Column(db.String(10), index=True, unique=False)
    district = db.Column(db.String(50), unique=False)
    latitude = db.Column(db.Float, index=True, unique=False)
    longitude = db.Column(db.Float, index=True, unique=False)

    # this tells python how to print a crime object
    def __repr__(self):
        return str(self.id) + ': ' + self.description

    # used by the endpoints to convert crime object into JSON
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
    first = db.Column(db.String(50), unique=False)
    last = db.Column(db.String(50), unique=False)
    middle = db.Column(db.String(50), unique=False, nullable=True)
    offense = db.Column(db.String(100), unique=False)
    date = db.Column(db.DateTime, index=True, unique=False)
    latitude = db.Column(db.Float, index=True, unique=False)
    longitude = db.Column(db.Float, index=True, unique=False)
    street = db.Column(db.String(70), unique=False)
    city = db.Column(db.String(50), unique=False)
    state = db.Column(db.String(2), unique=False)

    def __repr__(self):
        return str(self.id) + ': ' + self.last + ', ' + self.first

    @property
    def serialize(self):
        return{
            'first': self.first,
            'last': self.last,
            'middle': self.middle,
            'date': self.date,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'street': self.street,
            'city': self.city,
            'state': self.state,
        }

