'''
This module makes transformations on samples, such as shifting key or bpm to match song
'''
import numpy as np
from music21 import key
import librosa
from librosa.effects import pitch_shift, time_stretch


def get_valid_key_range(original_key, steps_range=2):
    '''
    Generate set keys within a range of the song key.
    
    Parameters:
        original_key (music21.Key):
            music21 key object of song.
        steps_range (Optional[int]):
            How many keys above and below to include in result.
    
    Returns:
        Set:
            music21 Key objects
    '''
    return { original_key.transpose(steps) : steps for steps in range(-steps_range, steps_range + 1) }


def get_candidate_sample_loops(sample_objects, original_tempo, original_key, require_key=True):
    '''
    Filters sample loops to those within the key and tempo range.
    
    Parameters:
        sample_objects (List[Sample]):
            List of created Sample objects
        original_tempo (int):
            tempo of song
        original_key (music21.Key):
            music21 key object of song.
        require_key (Optional[boolean]):
            Whether or not we want those in valid key range
    
    Returns:
        List[Sample]:
            filtered Sample objects
    '''
    candidate_samples = []
    valid_key_range = get_valid_key_range(original_key)
    
    for sample in sample_objects:
        if sample.tempo and abs(sample.tempo - original_tempo) < 10:
            if require_key:
                if sample.key and sample.key in valid_key_range:
                    candidate_samples.append(sample)
            else:
                if not sample.key or sample.key in valid_key_range:
                    # Basically this could be provided as an option if you want beats/FX/risers included
                    candidate_samples.append(sample)
    
    # TODO: consider switching data type to set if list is too slow/large
    return candidate_samples


# TODO: other get_candidate_sample_X types of calls, i.e. get_candidate_sample_one_shots or get_candidate_sample_<instrument>


def match_sample(sample, song_key, song_tempo, sample_rate=44100, mono=True):
    '''
    Matches a sample to have the same key (transpose) and tempo (time stretch) as song.
    
    Parameters:
        sample (Sample):
            Sample object to match
        song_key (music21.Key):
            music21 key object of song.
        song_tempo (int):
            tempo of song.
        sample_rate (Optional[int]):
            Sample rate to use for processing.
        mono (Optional[boolean]):
            Process in 1 channel if True, 2 channels (stereo) if False
    
    Returns:
        numpy.ndarray:
            matched sample in librosa format
    '''
    
    
    # TODO: figure out if sample should be transposed -> tempo matched, or tempo matched -> transposed
    
    # This could maybe be 2 separate functions, but need to analyze if it's best not to
    # save and load WAV files via librosa too often    
    print('Updating Tempo and Key for sample: ', sample.name)

    # Match Key if applicable
    transpose_steps = 0
    if sample.key:
        valid_key_range = get_valid_key_range(song_key)
        transpose_steps = -1 * valid_key_range[sample.key] # Direct the transposition towards the song key
        print('Transpose steps: ', transpose_steps)
    current_sample, sample_rate = librosa.load(sample.full_path, sr=sample_rate, mono=mono)    
    current_sample = pitch_shift(current_sample, sample_rate, n_steps=transpose_steps)
    
    # Match Tempo if applicable
    stretch_factor = 1
    if sample.tempo:
        stretch_factor = song_tempo / sample.tempo
        print('Stretch factor: ', stretch_factor)
    
    return time_stretch(current_sample, stretch_factor)


def loop_sample(song_file, sample_file, sample_rate=44100, mono=True):
    '''
    Repeats the sample n times to match length of song.
    
    Parameters:
        song_file (str):
            Path to wav file of song
        song_file (str):
            Path to wav file of sample to match length
        sample_rate (Optional[int]):
            Sample rate to use for processing.
        mono (Optional[boolean]):
            Process in 1 channel if True, 2 channels (stereo) if False
    
    Returns:
        numpy.ndarray:
            matched sample in librosa format
    '''
    current_song, sample_rate = librosa.load(song_file, sr=sample_rate, mono=mono)
    current_sample, sample_rate = librosa.load(sample_file, sr=sample_rate, mono=mono)
    repeat_times = int(round(len(current_song) / len(current_sample)))
    print('Repeating ' + str(repeat_times) + ' times')
    
    looped_sample = np.array([])
    for i in range(repeat_times):
        looped_sample = np.append(looped_sample, current_sample)
    
    return looped_sample