"""
Test for the Calculations class.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide


@pytest.fixture
def setup_calculations():
    """
    Setup fixture that clears history and adds sample calculations.
    """
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('3'), Decimal('2'), add))
    Calculations.add_calculation(Calculation(Decimal('7'), Decimal('2'), subtract))
    Calculations.add_calculation(Calculation(Decimal('4'), Decimal('2'), multiply))
    Calculations.add_calculation(Calculation(Decimal('6'), Decimal('2'), divide))


def test_add_calculation(setup_calculations):
    """
    Test adding a calculation to the history.
    """
    Calculations.clear_history()  # Ensure a clean slate
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"


def test_get_history(setup_calculations):
    """
    Test retrieving the entire calculation history.
    """
    history = Calculations.get_history()
    assert len(history) == 4, f"History has incorrect number of calculations: {len(history)}"


def test_clear_history():
    """
    Test clearing the entire calculation history.
    """
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"


def test_get_latest(setup_calculations):
    """
    Test getting the latest calculation from the history.
    """
    latest = Calculations.get_latest()
    assert latest.a == Decimal('6') and latest.b == Decimal('2'), "Incorrect latest calculation"


def test_find_by_operation(setup_calculations):
    """
    Test finding calculations in the history by operation type.
    """
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Incorrect number of calculations with add operation"

    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Incorrect number of calculations with subtract operation"


def test_get_latest_with_empty_history():
    """
    Test getting the latest calculation when the history is empty.
    """
    Calculations.clear_history()
    assert Calculations.get_latest() is None
