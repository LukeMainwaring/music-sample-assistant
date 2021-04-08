import os

from flask import Flask, send_file
app = Flask(__name__)

import glob
import os
import json
import soundfile as sf

from sample_parser import parse_sample_bpm, parse_sample_key
from sample_processor import Sample
from sample_transform import get_valid_key_range, get_candidate_sample_loops, match_sample
from music21 import key

# TODO: remove after these test sample filenames are no longer needed
disco_strings_file = 'test_samples/SC_DS_120_strings_stabs_swinging_upward_sting_Gmin.wav'
kshmr_guitar_file = 'test_samples/KSHMR_Latin_GTR_Guitar_90_Am.wav'
SPLICE_SAMPLES_PATH = '/Users/lukemainwaring/Splice/sounds/packs'

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
    sample_rate = 44100

    candidate_samples = find_candidate_samples(original_key, original_tempo)

    for sample in candidate_samples:
        matched_sample = match_sample(sample, original_key, original_tempo)
        sf.write('test_samples/candidate_samples_matched/' + sample.name, matched_sample, sample_rate)
        print('--------------------------------------\n')
    
    return 'Done'

# TODO: figure out how to send back multiple files once I have a UI to consume them
@app.route('/api/downloadAudio')
def download_wav_test():
    try:
        return send_file('/Users/lukemainwaring/ml/music-sample-assistant/msa-server/test_samples/KSHMR_Latin_GTR_Guitar_90_Am.wav',
            attachment_filename='test_audio.wav', as_attachment=True)
    except Exception as e:
        return str(e)


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
    # Hardcoded for now
    original_key = key.Key('C')
    original_tempo = 120

    sample_objects = create_sample_objects()
    candidate_samples = get_candidate_sample_loops(sample_objects, original_tempo, original_key)
    return candidate_samples

