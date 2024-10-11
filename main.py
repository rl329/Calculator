import os
import importlib
import pkgutil
from calculator.calculator import Calculator
from decimal import Decimal

# Function to dynamically load commands from the plugins directory
def load_plugins():
    plugins = {}
    package = 'calculator.plugins'
    plugin_path = os.path.join(os.path.dirname(__file__), 'calculator', 'plugins')

    for _, module_name, _ in pkgutil.iter_modules([plugin_path]):
        module = importlib.import_module(f"{package}.{module_name}")

        # Find classes that match the pattern "Command"
        for attr in dir(module):
            cls = getattr(module, attr)
            if isinstance(cls, type) and cls.__name__.endswith('Command'):
                plugins[module_name] = cls  # Register command class by its module name
    return plugins

# Show the menu (initially only the 'menu' option)
def show_initial_menu():
    print("Available options:")
    print(" - menu (to display available commands)")
    print(" - quit (to exit the program)")

# Show the available commands after typing 'menu'
def show_menu(available_commands):
    # Specify the desired order of commands
    command_order = ['add', 'subtract', 'multiply', 'divide']

    print("Available commands:")
    for command in command_order:
        if f"{command}_command" in available_commands:
            print(f" - {command}")
    print(" - quit (to exit the program)")


# REPL (Read-Eval-Print-Loop) function
def repl():
    calculator = Calculator()
    commands = load_plugins()  # Dynamically load commands

    # Show the initial menu with 'menu' and 'quit' only
    show_initial_menu()

    while True:
        user_input = input("Enter command (menu or quit): ").strip().lower()

        # Exit if the user types 'quit'
        if user_input == "quit":
            break

        # If user types 'menu', display all available commands
        elif user_input == "menu":
            show_menu(commands.keys())
            continue

        # Handle math operations after 'menu' is shown
        try:
            a = Decimal(input("Enter the first number: "))
            b = Decimal(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        # Execute the corresponding command class if it exists
        if f"{user_input}_command" in commands:
            command = commands[f"{user_input}_command"](calculator, a, b)
            result = command.execute()
            print(f"The result of {user_input} operation is: {result}")
        else:
            print("Invalid command!")

if __name__ == "__main__":
    repl()
