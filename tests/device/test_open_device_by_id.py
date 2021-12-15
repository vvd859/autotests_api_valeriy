import pytest


@pytest.mark.parametrize("relay, delay", [(1, 5), (0, 1)])
def test_positive(base_fixture, relay, delay):
    session_token = base_fixture.configs.token
    device_id = base_fixture.configs.device_id

    # response = base_fixture.api.devices.open_device_by_id(session_token, device_id, relay, delay)
    #
    # assert response.status_code == 202
