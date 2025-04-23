"""
Unit tests for the Calculation class in the calculator module.
"""

from decimal import Decimal
import pytest
from calculator.Calculation import Calculation
from calculator.operations import add,subtract,multiply,divide


@pytest.mark.parametrize("value1, value2, operation, expected",
[
    (Decimal('2'), Decimal('3'), add, Decimal('5')), # Addition : 2 + 3 = 5
    (Decimal('5'), Decimal('3'), subtract, Decimal('2')), # Subtraction : 5 - 3 = 2
    (Decimal('15'), Decimal('3'), divide, Decimal('5')), # Division : 15 / 3 = 5
    (Decimal('4'), Decimal('3'), multiply, Decimal('12')), # Multiply : 4 * 3 = 12
    (Decimal('3'), Decimal('3'), add, Decimal('6')) # Addition : 3 + 3 = 6
]
)

def test_calculate(value1: Decimal, value2: Decimal, operation, expected):
    ''' Test Calculation object computes correct results for the operations. '''
    obj = Calculation(value1, value2, operation)
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
