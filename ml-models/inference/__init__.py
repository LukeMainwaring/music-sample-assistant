from flask import Flask

import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import kapre
import numpy as np

def create_app():
    inference = Flask(__name__)

    kapre_objects = {'STFT':kapre.time_frequency.STFT,
                    'Magnitude':kapre.time_frequency.Magnitude,
                    'ApplyFilterbank':kapre.time_frequency.ApplyFilterbank,
                    'MagnitudeToDecibel':kapre.time_frequency.MagnitudeToDecibel}

    model = load_model('basic_cnn_samples.h5',
                            custom_objects=kapre_objects)
    
    @inference.route('/predict')
    def predict():
        with open('test_batch.npy', 'rb') as f:
            test_batch = np.load(f)
        predictions = model.predict(test_batch)
        return str(predictions)

    return inference