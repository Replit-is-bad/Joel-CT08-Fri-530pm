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
order = input('What would you like to order? y/n')

while order != 'n':
    if order in menu:
        print(f"Great! {order} costs ${menu[order]:.2f}.")
        
    else:
        print(order + " is not on the menu.")
    
order = input('What would you like to order? y/n')
