import configparser


class Config:

    def getConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read('properties/sit.ini')
        return self.config

    def getApiConfig(self):
        self.config = configparser.ConfigParser()
        self.config.read('properties/sit.ini')
        return self.config['API']
