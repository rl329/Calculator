"""
My Calculator Test
"""

import pytest
from calculator.calculator import Calculator

def test_add():
    """Test that the addition function works."""
    assert Calculator.perform_operation(2, 2, "add") == 4

def test_subtract():
    """Test that the subtraction function works."""
    assert Calculator.perform_operation(2, 2, "subtract") == 0

def test_multiply():
    """Test that the multiplication function works."""
    assert Calculator.perform_operation(2, 2, "multiply") == 4

def test_divide():
    """Test that the division function works."""
    assert Calculator.perform_operation(2, 2, "divide") == 1

def test_divide_by_zero():
    """Test that dividing by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Calculator.perform_operation(2, 0, "divide")
