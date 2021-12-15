import requests
import copy
from config import Config


class ApiDevices:
    def __init__(self):
        self.url = Config.url
        self.default_headers = {"accept": "application/json"}

    def open_device_by_id(self, token, device_id, relay, delay):
        api_method = f"/api/v4/devices/{device_id}/open"
        url = self.url + api_method
        resp_dict = {
            "relay": relay,
            "delay": delay
        }

        headers = copy.deepcopy(self.default_headers)
        headers['Authorization'] = token

        # response = requests.post(url, headers=headers, json=resp_dict)
        # print(response.text)
        # print(response.url)
        # return response
