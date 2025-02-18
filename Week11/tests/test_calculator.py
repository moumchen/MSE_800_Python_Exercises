import pytest
from ..mypackage.calculator import add, subtract, multiply, divide, factorial, is_prime, power

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

def test_factorial():
    assert factorial(5) == 120

def test_factorial_zero():
    with pytest.raises(ValueError, match="Cannot calculate factorial of 0"):
        factorial(0)

def test_is_prime():
    assert is_prime(11) is True

def test_is_prime_not():
    assert is_prime(10) is False

def test_power():
    assert power(2, 2) == 4
