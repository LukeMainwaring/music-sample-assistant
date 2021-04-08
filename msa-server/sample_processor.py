'''
Creates a Sample object from just the filename
'''
import logging
import json
from sample_parser import parse_sample_bpm, parse_sample_key

# LOGGER = logging.getLogger(__name__)


class Sample:
    '''Every sample will be an instance of this sample class'''
    def __init__(self, name, full_path=None, tempo=None, key=None, one_shot=False):
        self.name = name
        self.full_path = full_path
        self.tempo = self.get_sample_tempo(name)
        self.key = self.get_sample_key(name)
        # For one_shot, assume all loops contain bpm/tempo in filename
        # It seems like many filenames are labeled with "_one_shot_" or "_loop_",
        # so that's another possible strategy to enhance the accuracy
        self.one_shot = False if self.tempo else True

    def get_sample_tempo(self, name):
        return parse_sample_bpm(name)
    
    def get_sample_key(self, name):
        return parse_sample_key(name)

    # Custom to_json since Key object is not JSON serializable
    def to_json(self):
        sample_dict = self.__dict__
        sample_dict['key'] = str(self.key)
        return sample_dict