#Python program to purchase single item
print("Welcome to our shop")
a=input("Enter the product name you need to buy:")
items=['101','Dairymilk','340','4']
if a==items[1]:
    print("product_id=",items[0])
    print("price=",items[2])
    b=int(input("Enter the quantity:"))
    
    if b>4:
        print("Out of stock!!!")
    else:
        m=b*340
        print("Total Amount=",m)
else:
    print("Sorry the product you entered is not available")
      

          
