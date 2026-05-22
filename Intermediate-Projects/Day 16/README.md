# Day 16: OOP Coffee Machine ☕

An object-oriented implementation of the classic Coffee Machine program from Angela Yu's *100 Days of Code: The Complete Python Pro Bootcamp*. This project demonstrates how to break down complex systems into modular, maintainable classes and objects.

## 📌 Project Overview
The program simulates a digital coffee vending machine using three distinct modules provided in the course setup. Unlike standard procedural code, this version leverages pre-written modules to manage the menu items, coffee preparation resources, and financial transactions independently.

## 📂 Project Structure
*   `main.py`: The core runner file containing the program execution loop and user interaction logic.
*   `menu.py`: Houses the `Menu` and `MenuItem` classes to manage available beverages (`espresso`, `latte`, `cappuccino`), their resource costs, and pricing.
*   `coffee_maker.py`: Contains the `CoffeeMaker` class to manage the machine's internal ingredients (Water, Milk, Coffee), check resource availability, and handle brewing.
*   `money_machine.py`: Contains the `MoneyMachine` class to process coin insertions (quarters, dimes, nickels, pennies), calculate change, verify payments, and manage total profits.

## 🚀 How It Works
1. **Dynamic Prompting**: The program fetches available drinks dynamically from the `Menu` module.
2. **Hidden Commands**: Entering `report` outputs the current state of both the coffee ingredients and the money machine. Entering `off` safely terminates the program execution.
3. **Automated Resource Checking**: Validates if enough ingredients are left to brew the chosen drink.
4. **Autonomous Transactions**: The money machine automatically calculates coin inputs, checks if the user provided enough funds, and dispenses exact change.

## 💻 Sample Code Implementation
Here is how the modules are integrated into `main.py`:

```python
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
```

## 🛠️ Requirements & Setup
*   Python 3.x installed on your local system.
*   Keep all files (`main.py`, `menu.py`, `coffee_maker.py`, `money_machine.py`) in the same root directory.

Run the program with:
```bash
python main.py
```
