"""
@author: Prithviraj Deshmane

@Description:
A simple coffee machine program

Input:
- 'latte', 'cappuccino' or 'espresso' as type of drink
- 'off' to turn the machine off
- 'report' to generate a list of resources still available in the machine. eg: water, milk, coffee
- asks for payment in different denominations of coins

Output:
- change from payment
- type of coffee drink that user wanted
"""

from art import drinks

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

money = 0.0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def generate_report():
    """Prints report of resources left in the machine"""
    for resource in resources:
        if resource == "coffee":
            measurement = "mg"
        else:
            measurement = "ml"
        print(f"{resource.capitalize()}: {resources[resource]}{measurement}")
    print(f"Money: ${money:.2f}")


def check_resources(drink):
    """checks if machine has enough resources to make the user's drink"""
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            return {"status": "error", "resource": ingredient}

    return {"status": "ok"}
    # return {"status": "error", "resource": "water"}


def is_choice_on_the_menu(choice):
    """checks if user order is on the menu"""
    for drink in MENU:
        if choice == drink:
            return True
    return False


def get_payment():
    """Takes the user's payment in coins"""
    print("Please insert coins")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickels = int(input("How many nickels? : "))
    pennies = int(input("How many pennies? : "))

    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

# track whether the machine is on or off
isMachineOn = True


def get_drink_price(drink):
    """Returns the cost of the drink"""
    return MENU[drink]["cost"]


def process_payment(cost, paid):
    """Processes payment"""
    return paid - cost


def make_coffee(drink):
    """Makes the coffee, updates machine resources and profit"""
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]


while isMachineOn:
    # get user choice
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Goodbye!")
        isMachineOn = False
        continue

    if choice == "report":
        generate_report()
        continue

    if not is_choice_on_the_menu(choice):
        print("Sorry, this machine cannot make this item, please choose again.")
        continue

    machine_state = check_resources(choice)

    if machine_state["status"] == "error":
        print(f'Sorry, there is not enough {machine_state["resource"]}')
        continue

    drink_cost = get_drink_price(choice)
    print(f"Price of {choice} is ${drink_cost:.2f}")

    payment = get_payment()
    print(f"Paid: ${payment:.2f}")

    balance_amount = process_payment(drink_cost, payment)
    if balance_amount < 0:
        print(f"Sorry, that's not enough money, ${payment:.2f} refunded.")
        continue

    if balance_amount == 0:
        print("Exact amount received, thank you!")
    else:
        print(f"Here is ${balance_amount:.2f} in change")

    money += drink_cost

    make_coffee(choice)
    print(drinks[choice])
    print(f"Here is your {choice}. Enjoy!")