'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    '''Test that the addition function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that the subtraction function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    ''' Test that the multiplication function works '''
    assert Calculator.multiply(2,2) == 4

def test_divide():
    ''' Test that the division function works '''
    assert Calculator.divide(2,2) == 1