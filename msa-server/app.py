import os

from flask import Flask
app = Flask(__name__)

from sample_parser import parse_sample_bpm
import sample_processor
import sample_transform


# Routes
@app.route('/')
def hello_world():
    return 'Hello, World!'


# TODO: get all data
@app.route('/api/allData')
def get_all_data():
    return 'getting all data'


# TODO: slightly borrowed from notebook tests, delete after verifying
@app.route('/api/testBpm')
def test_bpm_parser():
    disco_fill_sample = 'TL_Loops_Drums_Disco_Fill_03_108.wav'
    sample_bpm = parse_sample_bpm(disco_fill_sample)
    return str(sample_bpm)