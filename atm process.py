#ATM PROCESS
print("Welcome")
print("Insert your card")
pin=int(input("Please enter your secret number:"))
if((pin>999 and pin<=9999) and (pin==2345)):
    print("valid pin")
else:
    print("invalid")
account=str(input("select account type:"))
if account=="savings" or account=="current":
    print("valid")
else:
    print("invalid")
amount=int(input("enter the amount:"))
print("PLEASE WAIT YOUR TRANSACTION IS PROCESSING")
totalamount=20000
currentbalance=totalamount-amount
print("currentbalance:",currentbalance)
print("please collect cash and remove card safely")
print("Thank you")
