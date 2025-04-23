"""
Unit tests for the Calculation class in the calculator module.
"""

from decimal import Decimal
import pytest
from calculator.Calculation import Calculation
from calculator.operations import add,subtract,multiply,divide

def test_calculate(a: Decimal, b: Decimal, operation, expected):
    ''' Test Calculation object computes correct results for the operations. '''
    obj = Calculation(a, b, operation)
    assert obj.calculate() == expected, f"Operation {operation.__name__} has been failed!!"

def test_repr():
    ''' Test that the string representation (__string_repr__) returns the expected format '''
    obj = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert obj.__string_repr__() == expected_repr

def test_dividebyzero():
    ''' Test that division by zero raises a ValueError with the correct message. '''
    obj = Calculation(Decimal('5'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Division By Zero is not allowed!"):
        obj.calculate()
