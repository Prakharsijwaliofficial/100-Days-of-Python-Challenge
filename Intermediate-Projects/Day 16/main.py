from menu import MenuItem, Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


# Create the physical machine components
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu() 
machine_on = True
while machine_on:
    # Use menu.get_items() to dynamically show choices: (espresso/latte/cappuccino/)
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the drink object first
        drink = menu.find_drink(choice)
        
        # If the drink exists in the menu
        if drink is not None:
            # Check resources, process payment, and make coffee using the methods
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print("Invalid selection. Please choose a valid drink.")
