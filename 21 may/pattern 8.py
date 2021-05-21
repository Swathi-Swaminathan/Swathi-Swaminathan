#pattern 8

res=2
for i in range(5):
    for j in range(5):
        if i<2 and res!=10 and res!=12 and res!=14 and res!=16 and res!=18 and res!=20: 
            print(" "+str(res),end=" ")
        else:
            print(str(res),end=" ")
        res+=2
    print(" ")
