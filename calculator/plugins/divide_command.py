from decimal import Decimal
from calculator.calculator import Calculator

class DivideCommand:
    def __init__(self, calculator, a: Decimal, b: Decimal):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.perform_operation(self.a, self.b, "divide")
