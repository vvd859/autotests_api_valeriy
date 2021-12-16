import pytest

from application import Application

fixture = Application()

@pytest.fixture(scope="session")
def base_fixture():
    return fixture