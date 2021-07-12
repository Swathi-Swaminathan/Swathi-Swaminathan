#pattern 46
res=2
for i in range(5,0,-1):
    for j in range(6,i,-1):
        print(""+str(res),end=" ")
        res+=2
    print()
