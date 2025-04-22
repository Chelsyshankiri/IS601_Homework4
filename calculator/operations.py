from decimal import Decimal

# Defines a function to add two numbers
def add(a: Decimal, b: Decimal) -> Decimal:
    '''
    Adds two numbers and returns the result
    '''
    return a + b

# Defines a function to subtract two numbers
def subtract(a: Decimal, b: Decimal) -> Decimal:
    '''
    Subtracts two numbers and returns the result
    '''
    return a - b

# Defines a function to multiply two numbers
def multiply(a: Decimal, b: Decimal) -> Decimal:
    '''
    Multiplies two numbers and returns the result
    '''
    return a * b

# Defines a function to divide two numbers
def divide(a: Decimal, b: Decimal) -> Decimal:
    '''
    Divides two numbers and returns the result
    '''
    if b == 0 :
        raise ValueError("Division By Zero is not allowed!")
    else:
        return a / b