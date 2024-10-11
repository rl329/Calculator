from calculator.calculator import Calculator
from calculator.command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from decimal import Decimal

def show_menu():
    """Displays available commands."""
    print("Available commands:")
    print(" - add")
    print(" - subtract")
    print(" - multiply")
    print(" - divide")
    print(" - menu (to display this menu)")
    print(" - quit (to exit the program)")

def get_command(calculator, operation, a, b):
    """Returns the appropriate command based on the operation."""
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
    """REPL loop for the calculator."""
    calculator = Calculator()

    # Display the menu when the REPL starts
    show_menu()

    while True:
        # Get user input
        user_input = input("Enter command (add, subtract, multiply, divide, menu, quit): ").strip().lower()

        # Exit the loop if the user types "quit"
        if user_input == "quit":
            break
        elif user_input == "menu":
            show_menu()
            continue

        # Handle the math operations (add, subtract, multiply, divide)
        try:
            a = Decimal(input("Enter the first number: "))
            b = Decimal(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        # Get the command based on the user's input and execute it
        command = get_command(calculator, user_input, a, b)
        if command:
            result = command.execute()
            print(f"The result of {user_input} operation is: {result}")

if __name__ == "__main__":
    print("Starting the calculator program...")
    repl()
