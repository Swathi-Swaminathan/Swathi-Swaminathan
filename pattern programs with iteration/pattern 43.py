#pattern 43
for i in range(1,6):
    res=i-1 
    for j in range(1,i+1):
        print(" "+str(res+i),end=" ")
        res+=2
    print()
