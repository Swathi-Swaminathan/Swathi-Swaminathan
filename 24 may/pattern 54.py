#pattern 54
n=5
res=1
for i in range(0,5):
    for j in range(0,i+1):
        print(""+str(res-i),end=" ")
        res+=1
    print()
