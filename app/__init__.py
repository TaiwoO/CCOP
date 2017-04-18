# this file describes behavior when the CCOP application is run

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate and configure the Flask application
app = Flask(__name__)
app.config.from_object('config')

# set up object-relational mapping
db = SQLAlchemy(app)

# import at the end prevents circular dependencies
# (views and models depend on app)
from app import views, models
