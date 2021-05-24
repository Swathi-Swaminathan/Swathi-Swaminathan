#pattern 55
n=4
res=1
for i in range(1,5):
    for j in range(1,i+1):
        print(""+str(res*res),end=" ")
        res+=1
    print()
