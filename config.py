from configparser import ConfigParser
import os
from pathlib import Path
root =  Path(__file__).parent

class GetDetails:
    def __init__(self):
       self.path = os.path.join(root, 'config.ini')


    def get_api_key(self):
        config = ConfigParser()
        config.read(self.path)
        api_key = config.get('Api', 'key')
        return api_key

    def get_twitter_consumer_key(self):
        config = ConfigParser()
        config.read(self.path)
        consumer_key = config.get('Twitter', 'consumer_key')
        return consumer_key

    def get_twitter_consumer_secret(self):
        config = ConfigParser()
        config.read(self.path)
        consumer_secret = config.get('Twitter', 'consumer_secret')
        return consumer_secret

    def get_twitter_access_token(self):
        config = ConfigParser()
        config.read(self.path)
        access_token = config.get('Twitter', 'access_token')
        return access_token

    def get_twitter_access_token_secret(self):
        config = ConfigParser()
        config.read(self.path)
        access_token_secret = config.get('Twitter', 'access_token_secret')
        return access_token_secret

    def get_sql_server_name(self):
        config = ConfigParser()
        config.read(self.path)
        self.sql_server_name = config.get('SQL', 'Server')

    def get_sql_database(self):
        config = ConfigParser()
        config.read(self.path)
        self.sql_database = config.get('SQL', 'Database')