from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add (a,b):
        """ Create and perform a calculation, then return the result. """
        calculation = Calculation(a, b, add)
        return calculation.get_result()
    
    @staticmethod
    def subtract(a, b):
        """Perform subtraction using the _perform_operation method."""
        calculation = Calculation(a, b, subtract)
        return calculation.get_result()
    
    @staticmethod
    def multiply(a,b):
        """Perform multiplication using the _perform_operation method."""
        calculation = Calculation(a, b, multiply)
        return calculation.get_result()
    
    @staticmethod
    def divide(a, b):
        """Perform division using the _perform_operation method."""
        calculation = Calculation(a, b, divide)
        return calculation.get_result()
    


