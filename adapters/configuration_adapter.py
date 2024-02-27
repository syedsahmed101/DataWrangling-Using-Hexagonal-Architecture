import json

'''
Description: Class to interface with the transformation configuration file.
'''
class ConfigurationAdapter:
    def __init__(self, config_file) -> None:
        self.config = config_file

    def load_configuration(self):
        with open(self.config, 'r') as file:
            return json.load(file)
