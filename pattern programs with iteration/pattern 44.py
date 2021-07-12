#pattern 44
res=0
for i in range(1,5):
    res+=i 
    for j in range(res,res-i,-1):
        print(""+str(j),end=" ")
    print()
