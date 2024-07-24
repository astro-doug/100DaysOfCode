# Requirements
# Makes 3 hot flavors
#   Espresso
#   Latte
#   Cappuccino
# Manages resources of water, milk, and coffee
# Coin operated - Penny, Nickel, Dime, Quarter
# Print report - resources remaining
# Take an order (hidden report and off options)
# Take coins (each type), and give change or give all back if not enough
# Check resources for ordered coffee and report if out of stock
# If all is well, deduct resources by amount per recipe, increase money, and make coffee

import data
import art
import os


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def display_resources() -> None:
    print("Current levels of supplies:")
    print(f"Water: {data.resources["water"]}ml")
    print(f"Milk: {data.resources["milk"]}ml")
    print(f"Coffee: {data.resources["coffee"]}g")
    print(f"Money: ${data.resources["money"]:.2f}")


def display_menu() -> None:
    print("MENU:")
    for key in data.MENU:
        print(f"{key.title()} -> ${data.MENU[key]["cost"]:.2f}")


def take_money(drink: str) -> float:
    cost: float = data.MENU[drink]["cost"]
    num_pennies: int = int(input("Number of Pennies: "))
    num_nickles: int = int(input("Number of Nickles: "))
    num_dimes: int = int(input("Number of Dimes: "))
    num_quarters: int = int(input("Number of Quarters: "))

    total_taken: float = float(num_pennies * data.coin_values["penny"] + num_nickles * data.coin_values["nickle"]
                               + num_dimes * data.coin_values["dime"] + num_quarters * data.coin_values["quarter"])

    print(f"Total money taken: ${total_taken:.2f}")
    return total_taken


def deposit_funds(amount: float) -> None:
    data.resources["money"] += amount


def give_change(drink: str, amount_taken: float) -> None:
    change: float = amount_taken - data.MENU[drink]["cost"]
    print(f"Change given: ${change:.2f}")


def check_resources(drink: str) -> str:
    low_resource: str = ""
    water_required: int = data.MENU[drink]["ingredients"]["water"]
    try:
        milk_required: int = data.MENU[drink]["ingredients"]["milk"]
    except KeyError:
        milk_required = 0
    coffee_required: int = data.MENU[drink]["ingredients"]["coffee"]

    if water_required > data.resources["water"]:
        low_resource = "water"
    elif milk_required > data.resources["milk"]:
        low_resource = "milk"
    elif coffee_required > data.resources["coffee"]:
        low_resource = "coffee"

    return low_resource


def brew_coffee(drink: str) -> None:
    data.resources["water"] -= data.MENU[drink]["ingredients"]["water"]
    try:
        data.resources["milk"] -= data.MENU[drink]["ingredients"]["milk"]
    except KeyError:
        data.resources["milk"] = data.resources["milk"]
    data.resources["coffee"] -= data.MENU[drink]["ingredients"]["coffee"]
    print()
    print(art.coffee_cup)
    print("Enjoy!")
    print()


def handle_order(drink: str) -> None:
    if drink.lower() not in ("espresso", "latte", "cappuccino"):
        print("\nInvalid order - please try again\n")
    else:
        low_resource: str = check_resources(drink)
        if low_resource == "":
            print(f"Order for {drink.title()}. That will be ${data.MENU[drink]["cost"]:.2f} please.")
            money_taken: float = take_money(drink)
            if money_taken >= data.MENU[drink]["cost"]:
                give_change(drink, money_taken)
                deposit_funds(data.MENU[drink]["cost"])
                brew_coffee(drink)
            else:
                print("Insufficient funds.")
        else:
            print(f"Sorry, there is insufficient {low_resource} to make your {drink}")


def take_order() -> None:
    global machine_operating
    display_menu()
    print()
    drink = input("How may we deliver your caffeine today: ")
    if drink.lower() == "report":
        display_resources()
    elif drink.lower() != "off":
        handle_order(drink)
    else:
        print("\nEntering maintenance mode.\n")
        machine_operating = False


if __name__ == "__main__":
    machine_operating: bool = True
    cls()
    print(art.coffee_machine)

    while machine_operating:
        print()
        take_order()
