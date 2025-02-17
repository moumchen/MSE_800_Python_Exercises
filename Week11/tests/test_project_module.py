
import pytest

from ..my_project import project_module

# This is a test function that uses the fixture defined in conftest.py
#       to compare with the expected value
def test_something(my_data):
    assert my_data == 42


# @pytest.mark.parametrize decorator is used to pass multiple values to the test function
# use assert to compare the result with the expected value
@pytest.mark.parametrize("values,expected_results",[
    (
    [1,2,3,4,5,6],
    [2.0, 3.0, 4.0, 5.0],
    ),
    (
    [-1, -2, -3, -4, -5, -6],
    [-2.0, -3.0, -4.0, -5.0],
    )
])
def test_rolling_average(values,expected_results):

    result = project_module.rolling_average(values, 3)
    assert result == expected_results
