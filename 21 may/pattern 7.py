#pattern 7

res=1
for i in range(5):
    for j in range(5):
        if i<2 and res!=11 and res!=13 and res!=15 and res!=17 and res!=19:
            print(" "+str(res),end=" ")
        else:
            print(str(res),end=" ")
        res+=2
    print(" ")
        
        
    
