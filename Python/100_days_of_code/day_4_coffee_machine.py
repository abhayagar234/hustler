# Build coffee machine
resources = {"ingredients": {"water": 300, "milk": 200, "coffee": 100}, "money": 0}


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return float(total)


# required resources to make chosen coffee
def required_resources(drink):
    recipes = {
        "Espresso": {
            "ingredients": {"water": 50, "milk": 0, "coffee": 18},
            "money": 1.5,
        },
        "Latte": {
            "ingredients": {"water": 200, "milk": 150, "coffee": 24},
            "money": 2.5,
        },
        "Cappuccino": {
            "ingredients": {"water": 250, "milk": 100, "coffee": 24},
            "money": 3.0,
        },
    }
    return recipes[drink]


def update_resources_report(drink):
    used_resources = required_resources(drink)
    for item in used_resources["ingredients"]:
        resources["ingredients"][item] -= used_resources["ingredients"][item]
    resources["money"] += used_resources["money"]
    return resources


def is_resource_sufficient(available, required):
    for item in required["ingredients"]:
        if available["ingredients"][item] < required["ingredients"][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def coffee_machine():
    is_on = True
    while is_on:
        choice = input(
            "What would you like to drink? (Espresso, Latte, Cappuccino) or would like to see the report or turn off the machine: "
        )
        if choice in ["Espresso", "Latte", "Cappuccino"]:
            drink_required_resources = required_resources(choice)

            if is_resource_sufficient(resources, drink_required_resources):
                print(f'{choice} will cost you ${drink_required_resources["money"]}.')
                total = process_coins()
                print(f"You have inserted ${total}.")

                if total >= drink_required_resources["money"]:
                    change = total - drink_required_resources["money"]
                    print(f"Here is ${change:.2f} in change.")

                    # Update the resources and serve the drink
                    update_resources_report(choice)
                    print(f"Here is your {choice}. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                print(
                    "Sorry, we cannot prepare the drink due to insufficient resources."
                )
        elif choice == "report":
            print("Updated resources report:", resources)
        else:
            is_on = False
            print("Machine turned off.")


coffee_machine()
