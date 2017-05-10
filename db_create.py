#!ccop_env/bin/python3
# author: Jody LeSage

# this file creates the empty database tables
from app import db
db.create_all()
