from flask import Flask, jsonify, after_this_request
app = Flask(__name__)

import base64
import glob
import os
import json
import soundfile as sf
import librosa
from music21 import key

from sample_parser import parse_sample_bpm, parse_sample_key
from sample_processor import Sample
from sample_transform import get_valid_key_range, get_candidate_sample_loops, match_sample
from util import get_music21_key

# TODO: remove after these test sample filenames are no longer needed
disco_strings_file = 'test_samples/SC_DS_120_strings_stabs_swinging_upward_sting_Gmin.wav'
kshmr_guitar_file = 'test_samples/KSHMR_Latin_GTR_Guitar_90_Am.wav'
SPLICE_SAMPLES_PATH = '/Users/lukemainwaring/Splice/sounds/packs'
TEMP_DIR = 'temp_samples/'
SAMPLE_RATE = 44100


# Routes
@app.route('/')
def hello_world():
    return 'Hello, World!'


# TODO: slightly borrowed from notebook tests, delete after verifying
@app.route('/api/testBpm')
def test_bpm_parser():
    sample_bpm = parse_sample_bpm(disco_strings_file)
    return str(sample_bpm)

@app.route('/api/testKey')
def test_key_parser():
    sample_key = parse_sample_key(kshmr_guitar_file)
    return str(sample_key)

@app.route('/api/getSpliceFiles')
def get_splice_files():
    sample_objects = create_sample_objects()
    return json.dumps([sample.to_json() for sample in sample_objects])


@app.route('/api/getCandidateSamples')
def get_candidate_samples():
    candidate_samples = find_candidate_samples()
    return json.dumps([sample.to_json() for sample in candidate_samples])

@app.route('/api/adjustCandidateSamples')
def adjust_candidate_samples():
    # Hardcoded for now
    original_key = key.Key('C')
    original_tempo = 120

    candidate_samples = find_candidate_samples(original_key, original_tempo)

    for sample in candidate_samples:
        matched_sample = match_sample(sample, original_key, original_tempo)
        sf.write('test_samples/candidate_samples_matched/' + sample.name, matched_sample, SAMPLE_RATE)
        print('--------------------------------------\n')
    
    return 'Done'

# TODO: figure out how to send back multiple files once I have a UI to consume them
@app.route('/api/downloadAudio')
def download_wav_test():
    kshmr_guitar_file = '/Users/lukemainwaring/ml/music-sample-assistant/msa-server/test_samples/KSHMR_Latin_GTR_Guitar_90_Am.wav'
    sample_name = 'KSHMR_Latin_GTR_Guitar_90_Am.wav'
    current_sample, sample_rate = librosa.load(kshmr_guitar_file, sr=SAMPLE_RATE, mono=True)
    temp_sample_file = TEMP_DIR + sample_name
    sf.write(temp_sample_file, current_sample, sample_rate)
    
    # Convert file to base64 before sending to UI
    encoded_data = encode_to_base64(temp_sample_file)

    response_data = { "sampleFileName": sample_name, "audioData": encoded_data }
    
    @after_this_request
    def remove_file(response):
        try:
            os.remove(temp_sample_file)
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response

    return jsonify(response_data)

@app.route('/api/getCandidateSamplesMatched/<song_key>/<tempo>')
def get_candidate_samples_matched(song_key, tempo):
    music21_key = get_music21_key(song_key)
    original_key = key.Key(music21_key)
    original_tempo = int(tempo)

    candidate_samples = find_candidate_samples(original_key, original_tempo)

    temp_sample_files = []
    response_data = []

    for sample in candidate_samples:
        temp_sample_file = TEMP_DIR + sample.name
        temp_sample_files.append(temp_sample_file)
        matched_sample = match_sample(sample, original_key, original_tempo)
        sf.write(temp_sample_file, matched_sample, SAMPLE_RATE)
        
        encoded_data = encode_to_base64(temp_sample_file)
        sample_reponse = { "sampleFileName": sample.name, "audioData": encoded_data }
        response_data.append(sample_reponse)        

    @after_this_request
    def remove_file(response):
        for temp_sample_file in temp_sample_files:
            try:
                os.remove(temp_sample_file)
            except Exception as error:
                app.logger.error("Error removing or closing downloaded file handle", error)
        return response
    
    return jsonify(response_data)

# Helper method to get all user's Splice files and convert to Sample objects
def create_sample_objects(splice_files=[]):
    splice_files = [sample_file.split('/')[-1] for sample_file in glob.glob(SPLICE_SAMPLES_PATH + '/**/*.wav', recursive=True)]
    
    # Get full file paths for Splice samples for eventual audio processing
    splice_files_path = glob.glob(SPLICE_SAMPLES_PATH + '/**/*.wav', recursive=True)
    full_file_path_map = { sample : sample_path for sample, sample_path in zip(splice_files, splice_files_path)}
    
    # Convert all Splice files to custom Sample object
    sample_objects = []
    for sample_file in splice_files:
        full_path = full_file_path_map[sample_file]
        new_sample = Sample(sample_file, full_path)
        sample_objects.append(new_sample)
    
    return sample_objects

# Helper method to find candidate samples for current song
def find_candidate_samples(original_key=None, original_tempo=120):
    sample_objects = create_sample_objects()
    candidate_samples = get_candidate_sample_loops(sample_objects, original_tempo, original_key)
    return candidate_samples

def encode_to_base64(sample_file):
    in_file = open(sample_file, "rb")
    data = in_file.read()
    in_file.close()
    return base64.b64encode(data).decode('ascii')