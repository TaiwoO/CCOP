#!ccop_env/bin/python3
# author: Jody LeSage

# this file runs the CCOP web app from the virtual environment
from app import app
# TODO set debug to False before final delivery
app.run(debug=False)
