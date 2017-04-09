# Running this file will build the db scheme

import sys
sys.path.insert(0, '../')

from app import app, db

with app.app_context():
    db.create_all()
