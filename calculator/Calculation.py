from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide

class Calculation:
    ''' This class is used to represent the arithmetic calculations which involves two decimal numbers and a operation. '''
    result = None
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        ''' Constructor for all the necessary attributes for Calculator object. '''
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self) -> Decimal:
        ''' This method returns the result of method call to the operation that need to perform by encapsulating the operation execution. '''
        return self.operation(self.a, self.b)

    @staticmethod
    def createCalculation(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        ''' This is a static method to create a calculation instance. '''
        return Calculation(a, b, operation)
    
    def __string_repr__(self):
        ''' Converts the instance to a string representation of the Calculation object which can be printed in a readable format '''
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
