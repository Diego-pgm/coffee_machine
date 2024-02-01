from menu import menu
from resources import resources, earnings

def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${earnings}")
    return True
    
def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
    return True

def check_transaction(drink):
    coins_inserted = process_coins()
    if drink['cost'] > coins_inserted:
        print('Sorry thats not enough money. Money refunded.')
        return False
    else:
        global earnings
        earnings = round(coins_inserted, 2)
        return True

def process_coins():
    coins = int(input("How many quarters (25)? ")) * 0.25 
    coins += int(input("How many dimes (10)? ")) * 0.10
    coins += int(input("How many nickel (5)? ")) * 0.05
    coins += int(input("How many pennies (1)? ")) * 0.01
    return coins
