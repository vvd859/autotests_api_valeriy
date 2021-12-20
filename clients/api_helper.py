from clients.stations_types import  ApiStationTypes
from clients.stations import ApiStations
class ApiHousehold:
    def __init__(self):
        self.station_types = ApiStationTypes()
        self.stations = ApiStations()
