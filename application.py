from clients.api_helper import ApiNvgr
from checkers.checkers_helper import Checkers
from config import Config


class Application:
    def __init__(self):
        self.configs = Config()
        self.api = ApiNvgr()
        self.checkers = Checkers()
        # self.helpers =

