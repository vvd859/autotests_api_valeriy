import pytest


def test_positive(base_fixture):
    session_token = base_fixture.configs.token
    response = base_fixture.api.station_types.get_configs_station_types()

    check_resp = base_fixture.checkers.station_types
    assert response.status_code == 200

@pytest.mark.parametrize("_name, _descr", [("A1", "A1"), ("B1", "B1")])
def test_post_data(base_fixture, _name, _descr):
    response = base_fixture.api.station_types.post_station_types(_name, _descr)
    assert response.status_code == 200
