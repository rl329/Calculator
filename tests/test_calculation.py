"""
Testing the operations that are being provided within the calculator.

"""

# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_addition_operation():
    """
    Testing the addition operation.
    """
    calc = Calculation(Decimal('3'), Decimal('2'), add)
    assert calc.perform() == Decimal('5')

def test_subtraction_operation():
    """
    Testing the subtraction operation.
    """
    calc = Calculation(Decimal('7'), Decimal('2'), subtract)
    assert calc.perform() == Decimal('5')

def test_multiplication_operation():
    """
    Testing the multiplication operation.
    """
    calc = Calculation(Decimal('4'), Decimal('2'), multiply)
    assert calc.perform() == Decimal('8')

def test_division_operation():
    """
    Testing the division operation.
    """
    calc = Calculation(Decimal('6'), Decimal('2'), divide)
    assert calc.perform() == Decimal('3')

def test_divide_by_zero():
    """
    Testing division by zero to ensure it raises a ValueError.
    """
    calc = Calculation(Decimal('7'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()

def test_calculation_repr():
    """
    Testing the string representation (__repr__) of the Calculation class.
    """
    calc = Calculation(Decimal('4'), Decimal('2'), add)
    expected_repr = "Calculation(4, 2, add)"
    assert repr(calc) == expected_repr
