menu = {
    # Seafood
    "Crab": 75.00,
    "Lobster": 120.00,

    # Meat mains
    "Ribeye Steak": 98.50,
    "Filet Mignon": 110.00,
    "Lamb Chops": 85.75,
    "Roast Duck": 72.25,

    # Other mains
    "Pasta": 18.99,
    "Salad": 12.50,

    # Drinks
    "Wine": 40.00,
    "Cocktail": 15.75,
    "Soda": 4.25,

    # Desserts
    "Cheesecake": 10.99,
    "Chocolate Cake": 11.50,

}



print('<------MENU------>')
print()
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")


print()
print('<---------------->')

orderhis = {}

order = ''

while order != 'n':
    order = input('What would you like to order?')
    if order != 'no more':
        
        if order in menu:
            print(f"Great! {order} costs ${menu[order]:.2f}.")
            print("*"*40)
            check = input('would u like to add it to ur order? Y/N ')
            if check == "y" :
                orderhis[order] = menu[order]
                print()
                print(order + ' has been added.')
                print()
                print(orderhis)
            elif check == 'n':
                print(order + ' not added')
            else:
                print(' *' + check + '* NOT FOUND')
    
        
        else:
            print(order + " is not on the menu. ")
            print("*"*40)
    elif order == 'no more':
        break

order_total = 0 
for order in orderhis.values():
    order_total += order

print('<------ORDER------>')
print()
for item, price in orderhis.items():
    print(f"{item}: ${price:.2f}")


print()
print('<---------------->')
print('TOTAL : $' + str(order_total))

        
        

    

