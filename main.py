from calculator.calculator import Calculator
from command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def get_command(calculator, operation, a, b):
    if operation == "add":
        return AddCommand(calculator, a, b)
    elif operation == "subtract":
        return SubtractCommand(calculator, a, b)
    elif operation == "multiply":
        return MultiplyCommand(calculator, a, b)
    elif operation == "divide":
        return DivideCommand(calculator, a, b)
    else:
        print("Invalid operation")
        return None

def repl():
    calculator = Calculator()
    while True:
        user_input = input("Enter command (add, subtract, multiply, divide) or 'quit' to exit: ").strip().lower()
        if user_input == "quit":
            break
        try:
            a = Decimal(input("Enter the first number: "))
            b = Decimal(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        command = get_command(calculator, user_input, a, b)
        if command:
            result = command.execute()
            print(f"The result of {user_input} operation is: {result}")

if __name__ == "__main__":
    repl()
