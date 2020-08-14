#! /usr/bin/python3

from flask import Flask
from flask_sslify import SSLify

import config
# from flaskDB import db

app = Flask(__name__)
sslify = SSLify(app)

