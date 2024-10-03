'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    """

    Testing the add function.

    """
    assert Calculator.add(4,3) == 7

def test_subtraction():
    """

    Testing the subtract function.

    """
    assert Calculator.subtract(4,3) == 1

def test_multiply():
    """

    Testing the multiply function.

    """
    assert Calculator.multiply(2,2) == 4

def test_divide():
    """

    Testing the divide function

    """
    assert Calculator.divide(2,2) == 1
