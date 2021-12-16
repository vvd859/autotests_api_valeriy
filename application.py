from clients.api_helper import ApiHousehold
from checkers.checkers_helper import Checkers
from config import Config


class Application:
    def __init__(self):
        self.configs = Config()
        self.api = ApiHousehold()
        self.checkers = Checkers()
        # self.helpers =

