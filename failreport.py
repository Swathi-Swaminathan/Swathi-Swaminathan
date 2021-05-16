#fail report
tamil=int(input("enter tamil mark:"))
english=int(input("enter english mark:"))
maths=int(input("enter maths mark:"))
science=int(input("enter science mark:"))
social=int(input("enter social mark:"))
count=0
if tamil>=35:
    print("tamil cleared")
else:
    print("tamil not cleared")
    count=count+1
if english>=35:
    print("english cleared")
else:
    print("english not cleared")
    count=count+1
if maths>=35:
    print("maths cleared")
else:
    print("maths not cleared")
    count=count+1
if science>=35:
    print("science cleared")
else:
    print("science not cleared")
    count=count+1
if social>=35:
    print("social cleared")
else:
    print("social not cleared")
    count=count+1
print("total no of subjects failed=",count)
    
