import os

from flask import Flask
app = Flask(__name__)

# Routes
@app.route('/')
def hello_world():
    return 'Hello, World!'


# TODO: get all data
@app.route('/api/allData')
def get_all_data():
    return 'getting all data'


# TODO: endpoints to grab specific data if helpful