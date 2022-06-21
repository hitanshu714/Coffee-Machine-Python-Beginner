from art import coffee_mug
import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
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

money_in_machine = 0


def get_user_input():
    return input("What would you like? Espresso/Latte/Cappuccino  :  ").lower()


def get_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    global money_in_machine
    money = money_in_machine
    print(f"Current resources available :\n Water : {water} ml\n Milk : {milk} ml\n Coffee : {coffee} gm"
          f"\n Money : ${money}")


def check_resources(order):
    for element in resources:
        if MENU[order]["ingredients"][element] > resources[element]:
            return element
    return "0"

#print(check_resources("espresso"))

def process_coins(order):
    cost = MENU[order]["cost"]
    global money_in_machine
    previous_amount = 0
    is_enough = False
    while not is_enough:
        quarters = int(input("How many quarters (0.25c) : "))
        dimes = int(input("How many dimes (0.10c) : "))
        nickels = int(input("How many nickels (0.05c) : "))
        pennies = int(input("How many pennies (0.01c) : "))
        total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies + previous_amount
        if cost > total:
            more=input(f"You total is only {total}, do you want to enter more coins? 'y'/'n' :  ").lower()
            if more == 'n':
                print(f"Insufficient funds, entered amount : {total} refunded")
                return 0
            else:
                previous_amount = total
        else:
            change = total - cost
            print(f"Your change is {change}")
            money_in_machine += cost
            is_enough = True
    return 1


def change_resources(order):
    for element in resources:
        resources[element] -= MENU[order]["ingredients"][element]


def make_coffee(order):
    enough = check_resources(order)
    if enough != "0":
        print (f"Insufficient {element}, cannot process order at this time.")
    else:
        is_payment = process_coins(order)
        if is_payment == 0:
            return 0
        else:
            change_resources(order)
            print("Here is you coffee! ")
            print(coffee_mug)
            print("Stay Healthy")
            return 1



def machine():
    still_coffee = True
    while still_coffee:
        print (coffee_mug)
        print("Welcome to the Coffee Machine")

        order = get_user_input()
        if order == "report":
            get_report()
        else:
            make_coffee(order)
            more = input("Do you want more? 'y' / 'n'  :  ").lower()
            if more == "y":
                os.system("cls")
            else:
                still_coffee = False
    print("\n\n Thank you for using this machine! ")


machine()