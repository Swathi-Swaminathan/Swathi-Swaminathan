#pattern 56
n=5
for i in range(1,6):
    res=i
    for j in range(1,i+1):
        print(""+str(res),end=" ")
        res=res+(n-j)
    print()
