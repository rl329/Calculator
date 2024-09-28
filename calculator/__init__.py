from typing import List
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    history: List[Calculation] = []

    @classmethod
    def perform_operation(cls, a: float, b: float, operation_name: str) -> float:
        if operation_name == "add":
            result = add(a, b)
        elif operation_name == "subtract":
            result = subtract(a, b)
        elif operation_name == "multiply":
            result = multiply(a, b)
        elif operation_name == "divide":
            result = divide(a, b)
        else:
            raise ValueError("Invalid operation")

        calculation = Calculation(a, b, operation_name, result)
        cls.history.append(calculation)
        return result

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()

    @classmethod
    def get_latest_calculation(cls) -> Calculation:
        return cls.history[-1] if cls.history else None
