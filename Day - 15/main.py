order = "latte"
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    order: {
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
    "water": 1000,
    "milk": 500,
    "coffee": 300,
    "money" : 0
}


def report():
    print(f"Water : {resources["water"]}ml")
    print(f"Milk : {resources["milk"]}ml")
    print(f"Coffee : {resources["coffee"]}gm")
    print(f"Money:{resources["money"]}")

def insert_money():
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickels = int(input("How many nickels?:"))
    pennies = int(input("How many pennies?:"))
    return 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies

def machine(orders):
    if resources["water"] >= MENU[orders]['ingredients']['water'] and resources["milk"] >= MENU[orders]['ingredients']['milk'] and resources["coffee"] >= MENU[orders]['ingredients']['coffee'] :
        print("Please insert coins.")
        money_inserted = insert_money()
        if money_inserted >= MENU[orders]['cost'] :
            if money_inserted > MENU[orders]['cost']:
                print(f'Here is ${round(money_inserted - MENU[orders]['cost'], 2)} dollars in change')
            resources["money"] += 1.50
            resources["water"] -= MENU[orders]['ingredients']['water']
            resources["milk"] -= MENU[orders]['ingredients']['milk']
            resources["coffee"] -= MENU[orders]['ingredients']['coffee']
            print(f"Here is your {orders} ☕. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry there are not enough ingredients.")

while True:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "report":
        report()
    elif order == "off":
        break
    else:
        machine(order)



