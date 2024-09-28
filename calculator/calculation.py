from decimal import Decimal
from typing import Callable

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> None:
        self.a = a
        self.b = b
        self.operation = operation
        
        @staticmethod
        def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
            return Calculation(a, b, operation)
        
        def perform_calculation(self) -> Decimal:
            return self.operation(self.a, self.b)

        def __repr__(self) -> str:
            return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
        
            