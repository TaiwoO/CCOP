#!/bin/bash

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
ccop_env/bin/pip3 install sqlalchemy-migrate
ccop_env/bin/pip3 install requests

# have yet to find a reason to have apache
# sudo apt-get install apache2

# Decided on SQLite instead
# install and setup mysql
# sudo apt-get install mysql-server
# sudo mysql_secure_installation
# sudo mysqld --initialize

# install python 2.7, pip, and the requests library
# sudo apt-get install python2.7
# sudo apt-get install python-pip
# sudo -H pip install --upgrade pip
# sudo -H pip install requests
