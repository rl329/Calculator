from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Command for Addition
class AddCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.perform_operation(self.a, self.b, "add")

# Concrete Command for Subtract
class SubtractCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.perform_operation(self.a, self.b, "subtract")

# Concrete Command for Multiplication
class MultiplyCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.perform_operation(self.a, self.b, "multiply")

# Concrete Command for Division
class DivideCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.perform_operation(self.a, self.b, "divide")
