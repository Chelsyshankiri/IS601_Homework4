''' My Calculator Test with Calculator emcapsulation'''
import pytest
from calculator import Calculator

def test_add():
    '''Tests the addition function with encapsulation'''
    result = Calculator.add(2,3)
    assert result == 5

def test_subtract():
    '''Tests the subtraction function with encapsulation'''
    assert Calculator.subtract(5,3) == 2


def test_multiply():
    '''Tests the multiplication function with encapsulation'''
    assert Calculator.multiply(4,5) == 20


def test_divide():
    '''Tests the division function with encapsulation'''
    assert Calculator.divide(10,2) == 5

def test_dividebyzero():
    '''Tests the division function in dividebyzero scenario with encapsulation'''
    with pytest.raises(ValueError):
        Calculator.divide(10,0)
