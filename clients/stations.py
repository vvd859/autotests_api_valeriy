import requests
import copy
from config import Config


class ApiStations:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}

    def get_station(self):
        api_method = "/api/Station"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        response = requests.get(url, headers=headers)
        return response

    def get_stations_id(self, _id):
        api_method = f"/api/Station/{_id}"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        response = requests.get(url, headers=headers)
        return response

    def post_stations(self, _id_station_type, _name, _descr):
        api_method = "/api/Station"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        _data = {
            "id_station_type": _id_station_type,
            "name": _name,
            "descr": _descr
        }
        response = requests.post(url, headers=headers, json=_data)
        return response

    def put_stations_id(self, _id, _station_type, _name, _descr):
        api_method = f"/api/Station/{_id}/{_station_type}"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        _data = {
            "name": _name,
            "descr": _descr
        }

        response = requests.put(url, headers=headers, json=_data)
        return response

    def delete_stations_id(self, _id):
        api_method = f"/api/Station/{_id}"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        response = requests.delete(url, headers=headers)
        return response

    def finder_stations_name(self, _name):
        api_method = f"/api/Station/FinderStationName"
        url = self.url + api_method

        headers = copy.deepcopy(self.default_headers)
        # headers['Authorization'] = token

        response = requests.get(url, headers=headers, params={"name":_name})
        return response
