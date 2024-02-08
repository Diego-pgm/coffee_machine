from menu import menu
from resources import resources, earnings
from functions import check_resources, report, check_transaction, make_coffee


is_on = True
while is_on:
    print('-----------Menu--------------')
    for item in menu:
        print(item)
    user_input = input('What would you like? ')
    
    if user_input == "off":
        is_on = False
    
    elif user_input == "report":
        report()

    else:
        drink = menu[user_input]
        if check_resources(drink['ingredients']) and check_transaction(drink):
            make_coffee(drink['ingredients'])
            print('Transaction successfull')
