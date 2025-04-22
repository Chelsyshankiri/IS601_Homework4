from calculator.operations import add, subtract, divide, multiply
from calculator.Calculation import Calculation
from calculator.calculations import calculations
from decimal import Decimal
from typing import Callable

class Calculator:
    ''' This is a class is to have static methods for performing the arithmetic operations like a calculator. '''
    @staticmethod
    def do_operation(value1: Decimal, value2: Decimal, operation: Callable[[Decimal,Decimal], Decimal]):
        ''' This method performs the specified arithmetic operation on two decimal numbers.
        The operation that is performed is passed as callable function (add, subtract, multiply, divide). '''
        calculation = Calculation.createCalculation(value1, value2, operation)
        calculations.add_history(calculation)
        return calculation.calculate()
    
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        ''' This method adds two decimal numbers and stores the calculations to the history. '''
        return Calculator.do_operation(a,b,add)


    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        ''' This method subtracts two decimal numbers and stores the calculations to the history. '''
        return Calculator.do_operation(a,b,subtract)


    @staticmethod
    def multiply(a: Decimal, b:Decimal) -> Decimal:
        ''' This method multiplies two decimal numbers and stores the calculations to the history. '''
        return Calculator.do_operation(a,b,multiply)


    @staticmethod
    def divide(a: Decimal, b:Decimal) -> Decimal:
        ''' This method divides two decimal numbers and stores the calculations to the history. '''
        return Calculator.do_operation(a,b,divide)