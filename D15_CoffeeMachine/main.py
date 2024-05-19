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
    "money": 0
}


DIMES = 0.10
QUARTERS =  0.25
NICKLES = 0.05
PENNIES = 0.01


def is_resource_sufficient(user_choice):
    '''Function to determine whether there is sufficient resources left for the machine'''
    drink_ingredients = MENU[user_choice]["ingredients"]
    for ingredient in resources:
        for drink_ingredient in drink_ingredients:
            if resources[ingredient] >= drink_ingredients[drink_ingredient]:
                return True
            else:
                print(f"Sorry. Insufficient {ingredient} resource")
                return False

def process_coins(user_choice):
    '''Function to process coins inputted by the user'''
    drink_cost = MENU[user_choice]["cost"]
    user_dimes = int(input("Please insert how many dimes you want ($0.10): "))
    user_quarters = int(input("Please insert how many quarters you want ($0.25): "))
    user_nickles = int(input("Please insert how many nickles you want ($0.05): "))
    user_pennies = int(input("Please insert how many pennies you want ($0.01): "))
    total_money = round((user_dimes * DIMES) + (user_quarters * QUARTERS) + (user_nickles * NICKLES) + (user_pennies * PENNIES), 1)

    if total_money >= drink_cost:
        transaction(total_money, drink_cost)
        make_drink(user_choice)
    else:
        print("Sorry that's not enough money. Money refuncded")


def transaction(total_money, drink_cost):
    '''Function to calculate the change and add the cost of the drink to the resources'''
    resources["money"] += drink_cost
    if total_money > drink_cost:
        change = round((total_money - drink_cost), 1)
        print(f"You have entered {total_money}. Here's your ${change} in change.")
    
    
def make_drink(user_choice):
    '''Function to deduct the ingredients used from the resources and give user their chosen drinks'''
    drink_ingredients = MENU[user_choice]["ingredients"]
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here's your {user_choice}. Enjoy!")


is_machine_running = True

#Main while loop
while is_machine_running is True:
    user_choice = input("What would you like? (espresso/latte/cappucino): ")
    if user_choice == "off":
        print("Machine turned off")
        is_machine_running = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml\n Milk: {resources['milk']}ml\n Coffee: {resources['coffee']}g\n Money: ${resources['money']}")
    elif user_choice == "espresso":
        if is_resource_sufficient(user_choice) == True:
            process_coins(user_choice)
        else:
            is_machine_running = False
    elif user_choice == "latte":
        if is_resource_sufficient(user_choice) == True:
            process_coins(user_choice)
        else:
            is_machine_running = False
    elif user_choice == "cappuccino":
        if is_resource_sufficient(user_choice) == True:
            process_coins(user_choice)
        else:
            is_machine_running = False
    else:
        print("You have entered an incorrect prompt. Please try again")