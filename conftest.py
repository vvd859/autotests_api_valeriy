import pytest

from applications import Application

fixture = Application()

@pytest.fixture(scope="session")
def base_fixture():
    return fixture