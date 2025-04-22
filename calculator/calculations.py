from calculator.Calculation import Calculation
from decimal import Decimal
from typing import Callable,List

class calculations:
    ''' This class is used to manage the history of arithmetic calculations. '''
    history = []

    @classmethod
    def add_history(cls,Calculation: Calculation):
        ''' Adds a instance of calculation to the history. '''
        cls.history.append(Calculation)
    
    @classmethod
    def delete_history(cls):
        ''' This classmethod will clear the data inside the history list. '''
        cls.history.clear()
        
    @classmethod
    def print_history(cls) -> List[Calculation]:
        '''  Return the list of Calculations in the history. '''
        return cls.history
    
    @classmethod
    def get_latest_history(cls):
        '''  This method retrives the most recent Calculation from the history. '''
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def get_with_operation(cls, operation:str) -> List[Calculation]:
        ''' This method will retrive the calculations that matches with the given operation. '''
        return [i for i in cls.history if i.operation.__name__ == operation]