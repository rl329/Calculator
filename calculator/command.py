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
        return self.calculator.add(self.a, self.b)

# Concrete Command for Subtraction
class SubtractCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.subtract(self.a, self.b)

# Concrete Command for Multiplication
class MultiplyCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.multiply(self.a, self.b)

# Concrete Command for Division
class DivideCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self):
        return self.calculator.divide(self.a, self.b)
