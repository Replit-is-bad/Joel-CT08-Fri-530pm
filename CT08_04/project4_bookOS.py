import time

def show_bookshoplist():
    print()
    print('<------ITEMS------>')
    print()
    for items, price in bookshop.items():
        print(f"{items}: ${price:.2f}")
    print()
    print('<---------------->')
    print()

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



#order list to print at the end
order_list = {}
#to save the order
order = ''

while order != 'n':
    time.sleep(1)
    show_bookshoplist()
    order = input('what do u need? : ')
    if order != 'no more':
        if order in bookshop:
            print(f"Great! {order} costs ${bookshop[order]:.2f}.")
            print('*'*40)
            Amount = input('How much ' +order+ ' do you need?')
            try:
                amount_int = int(Amount)
                print(f'{amount_int} {order}(s) added to cart')
                # nested dictionary
                order_list[order] = {"amount" : amount_int, "Price" : bookshop[order]}
            except ValueError:
                print('Invalid amount, please enter a number.')
                continue
        else:
            print(' ERROR ' + order + ' IS NOT IN THE BOOKSHOP')
            time.sleep(2)
    elif order == 'no more':
        break

order_total = 0 
for details in order_list.values():
    order_total += details["amount"] * details["Price"]

print('<------ORDER------>')
print()
for item, details in order_list.items():
    amount = details["amount"]
    price = details["Price"]
    item_total = amount * price
    print(f"{item}: {amount} @ ${price:.2f} each - ${item_total:.2f}")


print()
print('<---------------->')
print('TOTAL : $' + str(order_total)) 
        
            




