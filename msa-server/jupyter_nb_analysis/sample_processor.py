import logging
import json
from sample_parser import parse_sample_bpm, parse_sample_key

# LOGGER = logging.getLogger(__name__)


class Sample:
    ''' Creates a Sample object from just the filename '''

    def __init__(self, name, full_path=None, tempo=None, key=None, one_shot=False):
        '''
        Create music21 key from string value of key.

        Parameters:
            name (str):
                Filename of sample.
            full_path (Optional[str]):
                Full path to sample wav file.
            tempo (Optional[int]):
                Tempo/BPM of sample.
            key (Optional[music21.Key]):
                Music21 key object for sample.
            one_shot (Optional[boolean]):
                Whether or not the sample is a one-shot or loop
        '''

        self.name = name
        self.full_path = full_path
        self.tempo = self.get_sample_tempo(name)
        self.key = self.get_sample_key(name)
        # For one_shot, assume all loops contain bpm/tempo in filename
        # It seems like many filenames are labeled with "_one_shot_" or "_loop_",
        # so that's another possible strategy to enhance the accuracy
        self.one_shot = False if self.tempo else True

    def get_sample_tempo(self, name):
        '''
        Get BPM of sample from filename if exists, otherwise designate as a one-shot.
        
        Parameters:
            sample_file (str):
                Filename of sample.
        
        Returns:
            int:
                integer BPM of sample file, or None if one-shot.
        '''
        return parse_sample_bpm(name)
    
    def get_sample_key(self, name):
        '''
        Get key of sample from filename if exists.

        Parameters:
            sample_file (str):
                Filename of sample.

        Returns:
            music21.Key:
                music21 Key object, or None.
        '''
        return parse_sample_key(name)

    def to_json(self):
        ''' Custom to_json since Key object is not JSON serializable '''
        sample_dict = self.__dict__
        sample_dict['key'] = str(self.key)
        return sample_dict