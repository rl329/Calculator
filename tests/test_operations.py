# pylint: disable=invalid-name
"""
Test for calculator operations.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_add_operation():
    """
    Test the addition operation.
    """
    calculation = Calculation.create(Decimal('5'), Decimal('2'), add)
    assert calculation.perform() == Decimal('7'), "Addition operation failed"

def test_subtract_operation():
    """
    Test the subtraction operation.
    """
    calculation = Calculation.create(Decimal('9'), Decimal('2'), subtract)
    assert calculation.perform() == Decimal('7'), "Subtraction operation failed"

def test_multiply_operation():
    """
    Test the multiplication operation.
    """
    calculation = Calculation.create(Decimal('2'), Decimal('4'), multiply)
    assert calculation.perform() == Decimal('8'), "Multiplication operation failed"

def test_operation(a, b, operation, expected):
    """Testing various operations
    """
    calculation = Calculation.create(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    """
    Testing the divide by zero exception
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('7'), Decimal('0'), divide)
        calculation.perform()
