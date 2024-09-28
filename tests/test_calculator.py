import pytest
from calculator.calculator import Calculator

def test_add():
    assert Calculator.perform_operation(2, 3, "add") == 5

def test_subtract():
    assert Calculator.perform_operation(5, 3, "subtract") == 2

def test_multiply():
    assert Calculator.perform_operation(3, 4, "multiply") == 12

def test_divide():
    assert Calculator.perform_operation(10, 2, "divide") == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.perform_operation(5, 0, "divide")
