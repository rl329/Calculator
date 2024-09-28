from decimal import Decimal

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation_name: str, result: Decimal) -> None:
        self.a = a
        self.b = b
        self.operation_name = operation_name
        self.result = result

    def __str__(self) -> str:
        return f"{self.a} {self.operation_name} {self.b} = {self.result}"
