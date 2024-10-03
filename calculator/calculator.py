from typing import List, Callable
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:
    history: List[Calculation] = []

    operations_map = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    @classmethod
    def perform_operation(cls, a: float, b: float, operation_name: str) -> float:
        try:
            operation_func = cls.operations_map[operation_name]
        except KeyError:
            raise ValueError("Error operation")

        result = operation_func(a, b)

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
