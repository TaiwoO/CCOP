#!/bin/bash

# this file is written to make the application easy to set up
# when run as root, it installs dependencies and
# sets up a python virtual environment in which to run

# update apt
sudo apt-get update

# install python 3
sudo apt-get install -y python3 python3-pip python3-venv

# set up the python virtual environment
python3 -m venv ccop_env

# install python dependencies to the development environment
ccop_env/bin/pip3 install wheel		# needed to build wheels
ccop_env/bin/pip3 install flask
ccop_env/bin/pip3 install flask-sqlalchemy
#ccop_env/bin/pip3 install sqlalchemy-migrate
ccop_env/bin/pip3 install requests
