from menu import menu
from resources import resources, earnings

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


def main():
    is_on = True
    while is_on:
        user_input = input('What would you like? ')
    
        if user_input == "off":
            is_on = False
    
        elif user_input == "report":
            report()

        else:
            drink = menu[user_input]
            if check_resources(drink['ingredients']):
                print('resources sufficient')
    return is_on

