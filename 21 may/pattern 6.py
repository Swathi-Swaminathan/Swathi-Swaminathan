#pattern 6
res=1
for i in range(5):
    for j in range(5):
        if i<2 and res!=10:
            print(" "+str(res),end=" ")
        else:
            print(str(res),end=" ")
            
        
        res+=1
    print(" ")
    

    
