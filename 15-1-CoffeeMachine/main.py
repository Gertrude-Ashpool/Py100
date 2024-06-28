MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


money = 0.0


# TODO 1: ask the user what they would like

def get_mode():
    """Ask the user what they would like"""
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return prompt


# TODO 4: check if resources are sufficient

def check_resources(drink):
    resource = ""
    requires = 0
    level = 0
    can_prepare = True

    print("That requires:")
    # Iterate over the list of ingredients required for the drink
    for ingredient, requirement in MENU[drink]["ingredients"].items():
        # create local variables
        resource = ingredient # which material to check
        requires = int(requirement) # how much of this material is required
        level = int(resources[resource]) # current level of this material

        # # Debug print statements
        # print(f"checking {resource} requirement")
        # print(f"needs {requires}")
        # print(f"Current level: {level}")

        if requires > level:
            print(f"Sorry, there is not enough {resource}.")
            can_prepare = False
    if not can_prepare:
        coffee_machine()
    else:
        return True

# TODO 5: process payment
def process_payment(drink):
    # declare local variables
    # coin's values in cents
    coins = {
        "quarters" : 25,
        "dimes" : 10,
        "nickles" : 5,
        "pennies" : 1,
    }
    inserted = 0 # amount inserted in cents
    cost = int(MENU[drink]["cost"] * 100) # cost of drink in cents
    print("Please insert coins.")
    print(f"{drink} costs $ {MENU[drink]["cost"]}")
    print(f"...or {cost} cents.")
    for coin, value in coins.items():
        inserted += (int(input(f"How many {coin}?: "))) * value
        print(f"Inserted {inserted} cents so far.")
    if inserted < cost:
        print(f"Sorry, that's not enough money. Money refunded")
        coffee_machine()
    elif inserted > cost:
        change = str(round((inserted - cost) / 100, 2))
        print(f"Here is {change} in change.")
        return True
    else:
        return True


# make coffee
def prepare_drink(drink):
    # deduct resources
    for ingredient, requirement in MENU[drink]["ingredients"].items():
        requires = requirement
        current_level = resources[ingredient]
        new_level = current_level - requires
        resources[ingredient] = new_level

        # # debugging messages
        # print(f"{drink} requires:")
        # print(f"{ingredient}: {requires}")
        # print(f"Current level of {ingredient}: {current_level}")
        # print(f"Deducting {requires} from {current_level}.")
        # print(f"Resulting in new level of {resources[ingredient]}")
    print(f"Here is your {drink}. Enjoy!")
    coffee_machine()

def coffee_machine():

    mode = get_mode()

    # TODO 2: turn off the machine
    # perform required actions as long as user does not prompt "off"

    while mode != "off":

    # TODO 3: print a report

        if mode == "report":
            for resource, level in resources.items():
                print(f"{resource}: {level}")
            print(f"${money}")
            coffee_machine()


        elif mode == "espresso" or mode == "latte" or mode == "capuccino":
            if check_resources(mode) and process_payment(mode):
                prepare_drink(mode)
            coffee_machine()

        # exit the program / turn the machine off if user prompts "off"
        break

coffee_machine()

