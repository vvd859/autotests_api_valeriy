import pytest
import allure


def test_get_data(base_fixture):
    session_token = base_fixture.configs.token
    response = base_fixture.api.station_types.get_station_types()

    check_resp = base_fixture.checkers.station_types
    assert response.status_code == 200

@pytest.mark.parametrize("_id", [1, 2, 3])
def test_get_data_id(base_fixture, _id):
    with allure.step("GET id_station_type."):
        response = base_fixture.api.station_types.get_station_types_id(_id)
        print(response)
        resp_dict =response.json()
    with allure.step("Проверка."):
        assert response.status_code == 200


# @pytest.mark.parametrize("_name, _descr", [("A1", "A1"), ("B1", "B1"), ("C1", "C1")])
# def test_post_data(base_fixture, _name, _descr):
#     response = base_fixture.api.station_types.post_station_types(_name, _descr)
#     assert response.status_code == 200

# @pytest.mark.parametrize("_id, _name, _descr", [(1, "Z1", ""), (2, "Y1", ""), (3, "X1", "")])
# def test_put_data(base_fixture, _id, _name, _descr):
#     response = base_fixture.api.station_types.put_station_types_id(_id, _name, _descr)
#     print(response)
#     assert response.status_code == 200

# @pytest.mark.parametrize("_id", [1, 2, 3])
# def test_delete_data(base_fixture, _id):
#     response = base_fixture.api.station_types.delete_station_types_id(_id)
#     print(response)
#     assert response.status_code == 200
