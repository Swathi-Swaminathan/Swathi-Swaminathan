cart = {}
price = 0
quantity = 0
total = 0
while True:
    print("1.Add item\n2.remove\n3.View\n4Exit")
    ch = int(input("Enter the your choice:"))

    if ch == 1:
        name = str(input("Enter the product name"))
        if name in cart.keys():
            input('The item is already there if you want to make change \n 1.add more items\n 2. remove some items\n')
            option = int(input('Enter your option:'))
            if option == 1:
                print("the existing Quantity in the cart is: ", quantity)
                newquantity = int(input("Enter the quantity of the item:"))
                quantity += newquantity
                total = price * quantity
                cart[name] = [price, quantity, total]
            elif option == 2:
                newquantity = int(input("Enter the quantity of the item you want to reduce:"))
                if newquantity == 0:
                    print('The quantity value is 0 so it is removed from the cart list')
                    cart.pop(name)
                else:
                    quantity -= newquantity
                    if quantity == 0:
                        print('The item is removed from the list')
                        cart.pop(name)
                    else:
                        print('The quantity has been changed')
                        total = price * quantity
                        cart[name] = [price, quantity, total]
        else:
             price = int(input("Enter the product price:"))
             quantity = int(input("Enter the quantity of the item:"))
             total = price * quantity
             cart[name] = [price, quantity, total]
    elif ch == 2:
        remove_item = str(input("Enter the item you want to remove:"))
        if remove_item in cart.keys():
            cart.pop(remove_item)
        else:
            print("The specified item is not in the cart")
    elif ch == 3:
        print(cart)
        print("Item\tPrice\tQuantity\tTotal")
        for i in cart.keys():
            print(i, end="    ")
            for j in cart[i]:
                print(j, end="\t\t")
            print()
    elif ch == 4:
        break
    else:
        print('Give a valid option.')
