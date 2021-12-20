import pytest
import allure
import json
from helpers.validSchema import isValidJSON

def test_get_data(base_fixture):
    session_token = base_fixture.configs.token
    response = base_fixture.api.stations.get_station()
    
    check_resp = base_fixture.checkers.stations
    assert response.status_code == 200

@pytest.mark.parametrize("_id", [5, 2, 8])
def test_get_data_id(base_fixture, _id):
    with allure.step("GET id_station_type."):
        response = base_fixture.api.stations.get_stations_id(_id)
        print(response)
        resp_dict = response.json()
    with allure.step("Проверка."):
        assert response.status_code == 200

        with open("schemas/stations.json", "r") as _f:
            _schema = json.load(_f)

        check_res = isValidJSON(resp_dict[0], _schema)
        assert check_res is True, "Error"

@pytest.mark.parametrize("_id_station_type, _name, _descr", [(2, "A1", "A1"), (2, "B1", "B1"), (8, "C1", "C1")])
def test_post_data(base_fixture, _id_station_type, _name, _descr):
    response = base_fixture.api.stations.post_stations(_id_station_type, _name, _descr)
    assert response.status_code == 200

@pytest.mark.parametrize("_id, _statoin_type, _name, _descr", [(1, 4, "Z1", ""), (10, 4, "Y1", ""), (11, 4, "X1", "")])
def test_put_data(base_fixture, _id,  _statoin_type, _name, _descr):
    response = base_fixture.api.stations.put_stations_id(_id,  _statoin_type, _name, _descr)
    print(response)
    assert response.status_code == 200

@pytest.mark.parametrize("_id", [1, 2, 3])
def test_delete_data(base_fixture, _id):
    response = base_fixture.api.stations.delete_stations_id(_id)
    print(response)
    assert response.status_code == 200
