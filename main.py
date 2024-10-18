import os
import importlib
import pkgutil
from calculator.calculator import Calculator
from decimal import Decimal
from calculator.command import Command
from multiprocessing import Process
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env
load_dotenv()

# Access environment variables
env_name = os.getenv("ENV_NAME", "production")  # Default to 'production' if not set
api_key = os.getenv("API_KEY")

print(f"Running in {env_name} mode")
print(f"Using API key: {api_key}")

# Dynamically load commands through plugins
def load_plugins():
    plugins = {}
    package = 'calculator.plugins'
    plugin_path = os.path.join(os.path.dirname(__file__), 'calculator', 'plugins')

    for _, module_name, _ in pkgutil.iter_modules([plugin_path]):
        module = importlib.import_module(f"{package}.{module_name}")

        for attr in dir(module):
            cls = getattr(module, attr)
            if isinstance(cls, type) and cls.__name__.endswith('Command'):
                plugins[module_name] = cls

    return plugins

def show_initial_menu():
    print("Options:")
    print("menu - Menu (to display available commands)")
    print("quit - Quit (to exit the program)")

def show_menu(available_commands):
    command_order = ['add', 'subtract', 'multiply', 'divide']
    print("\nAvailable commands:")
    for command in command_order:
        if f"{command}_command" in available_commands:
            print(f"- {command}")
    print("- quit (to exit the program)")

def run_command(command_cls, calculator, a, b):
    result = command_cls(calculator, a, b).execute()
    print(f"The solution for {command_cls.__name__.replace('Command', '')} is: {result}")

def repl():
    calculator = Calculator()
    commands = load_plugins()

    show_initial_menu()

    while True:
        user_input = input("Enter Command (Menu or Quit): ").strip().lower()

        if user_input == "quit":
            break
        elif user_input == "menu":
            show_menu(commands.keys())
            continue

        try:
            a = Decimal(input("Enter the first number: "))
            b = Decimal(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue

        if f"{user_input}_command" in commands:
            command_cls = commands[f"{user_input}_command"]
            process = Process(target=run_command, args=(command_cls, calculator, a, b))
            process.start()
            process.join()
        else:
            print("Invalid command!")

if __name__ == "__main__":
    repl()
