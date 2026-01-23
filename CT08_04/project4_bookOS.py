# To store the item
bookshop = {
    'NO':500.50,
    'fart':3.00,
    'help':5.90,
    'pen':2.80,
    'Air-con':1999.69,
    'Acer-Predator-Helios-18-AI': 4999.99
}

print('Welcome to the bookshop!')
print()
#Prints the item list
print('<------ITEMS------>')
print()
for items, price in bookshop.items():
    print(f"{items}: ${price:.2f}")
print()
print('<---------------->')
print()

#order list to print at the end
order_list = {}
#to save the order
order = ''

