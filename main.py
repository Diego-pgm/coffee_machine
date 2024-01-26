from menu import menu


print('-----------Menu--------------')
for item in menu:
    print(item)

is_on = True
while is_on:
    user_input = input('What would you like? ')
    if user_input == "off":
        is_on = False
