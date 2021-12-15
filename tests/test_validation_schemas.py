# import jsonschema
import pytest
import json
from helpers.validSchema import isValidJSON

def test_valid_station():
    _data = {
        "id_station": 1,
        "id_station_type": 1,
        "name": "name",
        "note": "note"
        }
    with open("schemas/stations.json", "r") as _f:
        _schema = json.load(_f)

    print (_schema)
    assert isValidJSON(_data, _schema) == True, "InValid Schema"
    pass