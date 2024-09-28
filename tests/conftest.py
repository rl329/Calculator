"""
Conftest.py
"""

import pytest
from calculator.calculator import Calculator

@pytest.fixture(autouse=True)
def reset_history():
    """
    Clear calculation history before each test.
    """
    Calculator.clear_history()
