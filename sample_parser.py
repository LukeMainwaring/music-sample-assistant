'''
Module to parse sample files in order to obtain attributes like BPM and Key
'''
import re
from music21 import key
import logging

# LOGGER = logging.getLogger(__name__) # TODO: figure out how to use a module-level logger
LOGGER = logging.getLogger('sample_parser')
LOGGER.setLevel(logging.INFO)


NOTES = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# These are all the possible identifiers I found in my Splice samples.
# Could be useful to also go through all of Jake's or another friend's
MAJOR_KEY_IDENTIFIERS = ['', 'maj', '_major', '#', '#maj', '#_major', 'b', 'bmaj', 'b_major']

MINOR_KEY_IDENTIFIERS = ['m', 'min', 'minor', '_minor', '#m', '#min', '#minor', '#_minor',
                         'bm', 'bmin', 'bminor', 'b_minor']

ALL_MAJOR_KEYS = [note + identifier for note in NOTES for identifier in MAJOR_KEY_IDENTIFIERS]

ALL_MINOR_KEYS = [note + identifier for note in NOTES for identifier in MINOR_KEY_IDENTIFIERS]



def parse_sample_bpm(sample_file):
    '''
    :param sample_file: Filename of sample
    :return: int
    '''
    valid_bpms = [int(x) for x in re.findall(r'\d+', sample_file) if int(x) <= 200 and int(x) >= 50]
    
    if len(valid_bpms) > 1:
        # TODO: handle filenames with multiple valid BPMs, or just ignore for now
        # Note: right now, returning None means it's incorrectly classified as one-shot...
        return None
    elif len(valid_bpms) == 0:
        # TODO: decide if this condition means you should classify sample as one-shot
        return None
    else:
        return valid_bpms[0]


def parse_sample_key(sample_file):
    '''
    :param sample_file: Filename of sample
    :return: music21 Key object
    '''
    sample_file = sample_file.lower()
    key = None
    is_minor = False
    
    # Check major keys
    for maj_key in ALL_MAJOR_KEYS:
        maj_key_regex = '.*_' + maj_key + '[._]'
        if re.match(maj_key_regex, sample_file):
            key = maj_key
            
    # Check minor keys
    for min_key in ALL_MINOR_KEYS:
        min_key_regex = '.*_' + min_key + '[._]'
        if re.match(min_key_regex, sample_file):
            key = min_key
            is_minor = True

    # map key to music21 object if sample filename contains it
    return create_music21_key(key, is_minor) if key else None




def create_music21_key(sample_key, is_minor=False):
    '''
    :param sample_key: string key identifier grabbed from sample
    :param is_minor: Whether or not the key is minor
    :return: music21 Key object
    '''
    # 1. Grab first letter. In music21, lowercase note is minor and uppercase is major
    note = sample_key[0] if is_minor else sample_key[0].upper()
    
    # Create music21 object
    if '#' in sample_key:
        sharp_note = note.lower()
        curr_idx = NOTES.index(sharp_note)
        shifted_idx = 0 if curr_idx == len(NOTES) - 1 else curr_idx + 1 # if G# -> Ab, otherwise move up one note
        note = NOTES[shifted_idx]
        return key.Key(note + '-') if is_minor else key.Key(note.upper() + '-')
    elif 'b' in sample_key[1:]: # Ignore first note character since key of B would cause an issue
        return key.Key(note + '-')
    else:
        return key.Key(note)



