from configparser import ConfigParser

def get_api_key():
    config = ConfigParser()
    config.read('config.ini')
    api_key = config.get('Api', 'key')
    return api_key