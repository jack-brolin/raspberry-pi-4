import os

config_variables = {
    "POSTGRES_HOST": os.getenv("POSTGRES_HOST"),
    "POSTGRES_PORT": os.getenv("POSTGRES_PORT"),
    "POSTGRES_USER": os.getenv("POSTGRES_USER"),
    "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    "POSTGRES_DB": os.getenv("POSTGRES_DB")
}


class Config(object):
    def __init__(self):
        self._config = config_variables

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]


class ServiceConfig(Config):

    @property
    def postgres_host(self):
        return self.get_property('POSTGRES_HOST')

    @property
    def postgres_port(self):
        return self.get_property('POSTGRES_PORT')

    @property
    def postgres_user(self):
        return self.get_property('POSTGRES_USER')

    @property
    def postgres_password(self):
        return self.get_property('POSTGRES_PASSWORD')

    @property
    def postgres_db(self):
        return self.get_property('POSTGRES_DB')


config_dict = dict(
    service_config=ServiceConfig()
)
