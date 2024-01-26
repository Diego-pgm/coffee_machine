from menu import menu


print('-----------Menu--------------')
for item in menu:
    print(item)


def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    

earnings = 0
resources = {
    "water": 100,
    "milk": 200,
    "coffee": 80
}

is_on = True
while is_on:
    user_input = input('What would you like? ')
    
    if user_input == "off":
        is_on = False
    
    elif user_input == "report":
        report()
