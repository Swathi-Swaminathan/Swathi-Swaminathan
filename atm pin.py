#atm pin
pin=int(input("enter your pin:"))
if((pin>999 and pin<=9999) and (pin%10==2 or pin%10==7)):
    print("valid pin")
else:
    print("invalid pin")
