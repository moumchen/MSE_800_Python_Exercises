import pytest


# This is a fixture that will be used in the tests
# if we use pytest.fixture()
# we can use this fixture in the test functions of the whole package
@pytest.fixture()
def my_data():
    return 42