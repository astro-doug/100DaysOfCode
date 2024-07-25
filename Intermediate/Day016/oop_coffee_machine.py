# OOP Implementation of Coffee Machine from Day 015
# Classes for Menu, CoffeeMaker, and MoneyMachine were defined for me
# Implementation in the classes is different than I would have done it, but the lesson was just about using
# existing classes/API

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import art
import os


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu() -> None:
    print("MENU:")
    menu: Menu = Menu()
    drink_name: str
    for drink_name in menu.get_items().split("/"):
        if drink_name != "":
            menu_item: MenuItem = menu.find_drink(drink_name)
            print(f"{menu_item.name} -> ${menu_item.cost:.2f}")


def handle_order(coffee_maker: CoffeeMaker, money_machine: MoneyMachine, drink_name: str) -> None:
    menu: Menu = Menu()
    drink: MenuItem = menu.find_drink(drink_name)
    if not drink:
        print("\nInvalid order - please try again\n")
    else:
        if coffee_maker.is_resource_sufficient(drink):
            print(f"Order for {drink.name}. That will be ${drink.cost:.2f} please.")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


def take_order(coffee_maker: CoffeeMaker, money_machine: MoneyMachine):
    global machine_operating
    display_menu()
    print()
    drink = input("How may we deliver your caffeine today: ")
    if drink.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink.lower() != "off":
        handle_order(coffee_maker, money_machine, drink)
    else:
        print("\nEntering maintenance mode.\n")
        machine_operating = False


if __name__ == "__main__":
    cls()
    machine_operating: bool = True
    coffee_maker: CoffeeMaker = CoffeeMaker()
    money_machine: MoneyMachine = MoneyMachine()

    print(art.coffee_machine)

    while machine_operating:
        print()
        take_order(coffee_maker, money_machine)

