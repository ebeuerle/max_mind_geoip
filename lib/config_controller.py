import os
import yaml

FILE_CONFIG = os.path.join(os.path.dirname(__file__), '../config/config.yml')
CONFIG = yaml.load(file(FILE_CONFIG, 'r'))
