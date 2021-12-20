# import jsonschema
import pytest
import json
from helpers import isValidJSON

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

def test_valid_station_type():
    _data = {
        "id_station_type": 1,
        "name": "name",
        "note": "note"
        }
    with open("schemas/station_types.json", "r") as _f:
        _schema = json.load(_f)

    print (_schema)
    assert isValidJSON(_data, _schema) == True, "InValid Schema"

def test_valid_station_fail():
    _data = {
        "id_station": "BlaBla",
        "id_station_type": 1,
        "name": "name",
        "note": "note"
        }
    with open("schemas/stations.json", "r") as _f:
        _schema = json.load(_f)

    print (_schema)
    assert isValidJSON(_data, _schema) is False, "InValid Schema"

def test_valid_station_type_fail():
    _data = {
        "id_station_type": "BlaBla1",
        "name": "name",
        "note": "note"
        }
    with open("schemas/station_types.json", "r") as _f:
        _schema = json.load(_f)

    print (_schema)
    assert isValidJSON(_data, _schema) is False, "InValid Schema"
