from menu import menu


print('-----------Menu--------------')
for item in menu:
    print(item)


def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    
def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True


earnings = 0
resources = {
    "water": 1000,
    "milk": 2000,
    "coffee": 800
}

is_on = True
while is_on:
    user_input = input('What would you like? ')
    drink = menu[user_input]
    
    if user_input == "off":
        is_on = False
    
    elif user_input == "report":
        report()

    else:
        if check_resources(drink['ingredients']):
            print('resources sufficient')
