import base64

# TODO: add more keys once key selection is nailed down in UI
MUSIC21_KEY_MAPPINGS = {
    'A major' : 'A',
    'B major' : 'B',
    'C major' : 'C',
    'D major' : 'D',
    'E major' : 'E',
    'A minor' : 'a',
    'B minor' : 'b',
    'C minor' : 'c',
    'D minor' : 'd',
}

def get_music21_key(key_value):
    '''
    Convert user-facing key names to music21 key names
    
    Parameters:
        key_value (str):
            Friendly name for key value.
    
    Returns:
        str:
            String identifier to create proper music21 key.
    '''
    return MUSIC21_KEY_MAPPINGS[key_value]


def encode_to_base64(sample_file):
    '''
    Encode .wav file to base64 format
    
    Parameters:
        sample_file (str):
            Filename of wav file
    
    Returns:
        str:
            binary format of wav file
    '''
    in_file = open(sample_file, "rb")
    data = in_file.read()
    in_file.close()
    return base64.b64encode(data).decode('ascii')