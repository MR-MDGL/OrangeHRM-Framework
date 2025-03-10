import os
from configparser import ConfigParser

cwd = os.path.abspath(os.path.join(os.getcwd(), os.pardir))  # Go one level up from 'utility'
config = ConfigParser()
config_path = os.path.join(cwd, 'configuration', 'config.ini')

if not os.path.exists(config_path):
    print(f"Config file not found at: {config_path}")
else:
    print(f"Config file found at: {config_path}")

config.read(config_path)
print(f"Sections found: {config.sections()}")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('commonInfo', 'URL')

    @staticmethod
    def getUsername():
        return config.get('commonInfo', 'USERNAME')

    @staticmethod
    def getPassword():
        return config.get('commonInfo','PASSWORD')

# ob = ReadConfig()
# print(ob.getApplicationURL())
# print(ob.getUsername())
# print(ob.getPassword())
