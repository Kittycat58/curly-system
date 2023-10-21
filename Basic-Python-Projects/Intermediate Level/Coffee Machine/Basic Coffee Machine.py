def check_resources(resources, required):
    if resources['water'] >= required['water']:
        if resources['milk'] >= required['milk']:
            if resources['coffee'] >= required['coffee']:
                return 1
            else:
                print("Sorry there is not enough coffee")
                return 0
        else:
            print("Sorry there is not enough milk")
            return 0
    else:
        print("Sorry there is not enough water")
        return 0

def order(item, resources):
    global MENU
    for key,value in MENU.items():
        if key == item:
            required = value['ingredients']
            possible = check_resources(resources, required)
            if possible == 1:
                money = payment()
                if money > value['cost']:
                    balance = money - value['cost']
                    resources['water'] -= required['water']
                    resources['milk'] -= required['milk']
                    resources['coffee'] -= required['coffee']
                    resources['money'] += value['cost']
                    print(f"Here is your Rs.{balance} change.\nHere is your {item} ☕ Enjoy!")
                    return resources
                else:
                    print("Sorry that's not enough money. Money refunded")
                    return resources
            else:
                return resources

def payment():
    note_200 = int(input("How many 200 ruppee notes: "))
    note_100 = int(input("How many 100 ruppee notes: "))
    note_50 = int(input("How many 50 ruppee notes: "))
    note_20 = int(input("How many 20 ruppee notes: "))
    note_10 = int(input("How many 10 ruppee notes: "))
    total = 200*note_200 + 100*note_100 + 50*note_50 + 20*note_20 + 10*note_10
    return total

def start(resources):
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "report":
            for keys,values in resources.items():
                print(keys,": ",values)
        elif user_choice == "off":
            break
        else:
            order(user_choice, resources)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

start(resources)