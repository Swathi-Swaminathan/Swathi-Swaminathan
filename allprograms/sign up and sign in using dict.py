#Python program for sign up and sign in using dictionary
print("Welcome to Gmail")
user={"swathi@gmail.com":["swat1710",7092186302],"shanaya@gmail.com":["shans2001",7092186300]}

while True:
    print("1.New User\n2.Existing User\n3.Exit")
    option=int(input())

    if(option==1):
        email=input("Email=")
        password=input("Password=")
        mobile=int(input("Mobile="))
        if email in user.keys():
                   print("Email Id Already Exists")
        else:
            user[email]=[password,mobile]
            print(user)


    elif(option==2):
        email=input("Email=")
        password=input("Password=")
        if email in user.keys() and password==user[email][0]:
            
                print("Login Successfull!!!")
        else:
            print("Incorrect email or password!!!")

    elif(option==3):
        print("EXIT!!!")
        break
        

    
                   
