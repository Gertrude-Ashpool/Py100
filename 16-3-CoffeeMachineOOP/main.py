from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

choice = ""

# perform required actions as long as user does not prompt "off"
while choice != "off":
    # TODO 1: ask the user what they would like
    choice = input(f"What would you like? ({menu.get_items()}) ").lower()
    # TODO 2: turn off the machine
    if choice == "off":
        break
    # TODO 3: print a report
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # TODO 4: Check if resource is sufficient
        # TODO 5: Process Payment
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Make coffee
            coffee_maker.make_coffee(drink)
