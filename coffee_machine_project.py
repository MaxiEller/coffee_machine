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
    "water": 500,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

fill = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

money_types = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01

}

def use_machine():
    #Turns Machine on(True) or off(False)
    on = True
    while on == True:
        #Check if all resources are filled for the selected Coffee
        check = True
        #List the missing resources which have to be refilled
        missing = []
        #Count inserted money for the selected coffee
        money = 0
        coffee = input("What would you like? (espresso/latte/cappuccino) ")
        if coffee in MENU:
            for ingredient, amount in MENU[coffee]['ingredients'].items():
                if amount > resources[ingredient]:
                    check = False
                    missing.append(ingredient)
            if check == False:
                empty = ", ".join(missing)
                print(f'Sorry there is not enough {empty}.')
                print('next customer')
            else:
                print(f'Please insert {MENU[coffee]["cost"]}$ ')
                for key, value in money_types.items():
                    num = int(input(f'How many {key} have been inserted? '))
                    money += value * num
                    if money >= MENU[coffee]["cost"]:
                        break
                    else:
                        print(f'{round(MENU[coffee]["cost"] - money, 2)}$ left')
                if money < MENU[coffee]["cost"]:
                    print('Sorry, that’s not enough money. Money refunded')
                else:
                    change = money - MENU[coffee]["cost"]
                    resources['money'] += MENU[coffee]["cost"]
                    print(f'Here is your {coffee}. Enjoy!')
                    print(f'Your change is {round(change, 2)}$')
                    print('next customer')
                    for ingredient, amount in MENU[coffee]['ingredients'].items():
                        resources[ingredient] -= amount
        elif coffee == 'report':
            print(resources)
        elif coffee == 'off':
            on = False
        elif coffee == 'refill':
            refill = input('What would you like to refill? [water, coffee, milk] ')
            resources[refill] = fill[refill]
        else:
            print('enter something valid')

use_machine()