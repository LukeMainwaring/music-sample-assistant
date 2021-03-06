
# TODO: expand upon these once key selection is nailed down in UI
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