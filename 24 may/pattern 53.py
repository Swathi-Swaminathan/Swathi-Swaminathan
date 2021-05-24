#pattern 53
n=5
for i in range(1,6):
    res=1
    for j in range(1,i+1):
        print(""+str(res),end=" ")
        res=res*(i-j)//j
    print()
