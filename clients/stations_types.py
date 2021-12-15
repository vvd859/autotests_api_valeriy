import requests
import copy
from config import Config


class ApiStationTypes:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}

    def get_configs_station_types(self):
        api_method = "/api/StationType"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        response = requests.get(url, headers=headers)
        return response

    def post_station_types(self, _name, _descr):
        api_method = "/api/StationType"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        _data = {
            "name": _name,
            "descr": _descr
        }
        response = requests.post(url, headers=headers, json=_data)
        return response
