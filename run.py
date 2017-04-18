#!ccop_env/bin/python3

# this file runs the CCOP web app from the virtual environment
from app import app
app.run(debug=True)
