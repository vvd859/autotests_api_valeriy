import requests
import copy
from config import Config


class ApiStationTypes:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}

    def get_station_types(self):
        api_method = "/api/StationType"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        response = requests.get(url, headers=headers)
        return response

    def get_station_types_id(self, _id):
        api_method = f"/api/StationType/{_id}"
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

    def put_station_types_id(self, _id, _name, _descr):
        api_method = f"/api/StationType/{_id}"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        _data = {
            "name": _name,
            "descr": _descr
        }

        response = requests.put(url, headers=headers, json=_data)
        return response

    def delete_station_types_id(self, _id):
        api_method = f"/api/StationType/{_id}"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        response = requests.delete(url, headers=headers)
        return response
