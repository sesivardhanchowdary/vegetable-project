veg = ['carrot', 'potato', 'onion', 'beetroot']
quty = [10, 14, 15, 60]
costprice = [20, 15, 10, 25]
sellingprice = [30, 20, 20, 40]
report = []
user_cart = []
user_quant = []

while True:
    print('\n====== VEGITABLE MARKET MANAGEMENT SYSTEM ======')
    print('1. Owner')
    print('2. User')
    print('3. Exit')
    ch = int(input('Choose an option: '))

    if ch == 1:
        Name = input('Enter Name: ')
        Password = int(input('Enter Password: '))
        if Name == 'Bhargav' and Password == 2003:
            print('\n********** OWNER **********')
            print('Vegetables:', veg)
            print('Quantities:', quty)
            print('Selling Prices:', sellingprice)
            print()
        else:
            print('Invalid credentials. Exiting Owner Section.')
            continue

        while True:
            print('\n--- Owner Menu ---')
            print('1. Add Item')
            print('2. Remove Item')
            print('3. Update Item')
            print('4. View Items')
            print('5. Revenue Report')
            print('6. Exit')
            choice = input('Choose an option: ')
            print()

            if choice == '1' or choice.lower() == 'add item':
                item = input('Enter the item: ')
                if item in veg:
                    print('Item already exists.')
                else:
                    veg.append(item)
                    q = float(input('Enter quantity: '))
                    cp = float(input('Enter cost price: '))
                    sp = float(input('Enter selling price: '))
                    quty.append(q)
                    costprice.append(cp)
                    sellingprice.append(sp)
                    print(f"{item} added successfully.")

            elif choice == '2' or choice.lower() == 'remove item':
                item = input('Enter the item: ')
                if item not in veg:
                    print('Item not available.')
                else:
                    idx = veg.index(item)
                    veg.pop(idx)
                    quty.pop(idx)
                    costprice.pop(idx)
                    sellingprice.pop(idx)
                    print(f"{item} removed from inventory.")

            elif choice == '3' or choice.lower() == 'update item':
                item = input('Enter item to update: ')
                if item in veg:
                    idx = veg.index(item)
                    itemqunty = int(input('Enter new quantity: '))
                    itemcp = float(input('Enter new cost price: '))
                    itemsp = float(input('Enter new selling price: '))
                    quty[idx] = itemqunty
                    costprice[idx] = itemcp
                    sellingprice[idx] = itemsp
                    print('Item updated successfully.')
                else:
                    print('Item not found.')

            elif choice == '4' or choice.lower() == 'view item':
                print('\n***** Inventory *****')
                print('Veg\tQty\tCostPrice\tSellingPrice')
                for v, q, cp, sp in zip(veg, quty, costprice, sellingprice):
                    print(f'{v}\t{q}\t{cp}\t\t{sp}')

            elif choice == '5' or choice.lower() == 'revenue':
                print('\n********** Total Revenue **********')
                print(report)
                print('\nveg\tin stock\tcost price\tselling price')
                print('*' * 50)
                for i in range(len(veg)):
                    print(veg[i], "\t\t", quty[i], "\t\t", costprice[i], "\t\t", sellingprice[i])
                print('*' * 50)

            elif choice == '6' or choice.lower() == 'exit':
                break
            else:
                print('Invalid option.')

    elif ch == 2:
        name = []
        phone_number = []
        total = 0

        while True:
            print('\n********** USER **********')
            print('1. Add to Cart')
            print('2. Remove from Cart')
            print('3. Modify Cart')
            print('4. View Cart')
            print('5. Billing')
            print('6. Exit')
            choice = input('Choose an option: ')
            print()

            if choice == '1' or choice.lower() == 'add cart':
                item = input('Enter a vegetable: ')
                qty = int(input('Enter quantity in kgs: '))
                if item in user_cart:
                    print('Item already in the cart.')
                else:
                    if item in veg:
                        user_cart.append(item)
                        user_quant.append(qty)
                        print('Item added to cart.')
                    else:
                        print('Item not available.')

            elif choice == '2' or choice.lower() == 'remove cart':
                item = input('Enter item to remove: ')
                if item not in user_cart:
                    print('Item not in cart.')
                else:
                    idx = user_cart.index(item)
                    user_cart.pop(idx)
                    user_quant.pop(idx)
                    print('Item removed from cart.')

            elif choice == '3' or choice.lower() == 'modify cart':
                item = input('Enter item to modify: ')
                if item in user_cart:
                    idx = user_cart.index(item)
                    new_qty = int(input('Enter new quantity: '))
                    user_quant[idx] = new_qty
                    print('Cart updated.')
                else:
                    print('Item not in cart.')

            elif choice == '4':
                print('\n***** Your Cart *****')
                if user_cart:
                    for c, q in zip(user_cart, user_quant):
                        print(f'{c} - {q} kgs')
                else:
                    print('Cart is empty.')

            elif choice == '5':
                n = input('Enter your name: ')
                phone = input('Enter your phone number (+91): ')
                if len(phone) == 10:
                    name.append(n)
                    phone_number.append(phone)
                    print('\n------ Bill ------')
                    total = 0
                    print('Item\tQuantity\tPrice\tTotal')
                    print('-' * 40)
                    for item, qty in zip(user_cart, user_quant):
                        idx = veg.index(item)
                        price = sellingprice[idx]
                        item_total = qty * price
                        total += item_total
                        print(f'{item}\t{qty} kg\t{price}\t{item_total}')
                        # Revenue Report
                        cost = costprice[idx]
                        profit = (price - cost) * qty
                        report.append(f'{item} -> Sold {qty}kg, Profit: ₹{profit}')
                        quty[idx] -= qty  # reduce stock
                    print('-' * 40)
                    print(f'Total Amount: ₹{total}')
                    print()
                else:
                    print('Invalid phone number.')

            elif choice == '6' or choice.lower() == 'exit':
                print('Exiting User Section.')
                break
            else:
                print('Invalid option.')

        user_cart.clear()
        user_quant.clear()

    elif ch == 3:
        print('Thank you! Exiting the program.')
        break

    else:
        print('Invalid choice. Please choose again.')
