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
        change = round(coins_inserted - drink['cost'], 2)
        print(f'Drink Cost: {drink["cost"]}')
        print(f'Coins inserted: {coins_inserted}')
        earnings += round(coins_inserted - change, 2)
        print(f'Here you have: {change}! Thank you!')
        return True

def make_coffee(drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]

def process_coins():
    coins = int(input("How many quarters (25)? ")) * 0.25 
    coins += int(input("How many dimes (10)? ")) * 0.10
    coins += int(input("How many nickel (5)? ")) * 0.05
    coins += int(input("How many pennies (1)? ")) * 0.01
    return coins
