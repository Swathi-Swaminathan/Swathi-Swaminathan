#python program to print series: 3, 4, 7, 8, 11, 12, ...
n=int(input())
print(n,end=",")
for i in range(n):
    a=n+1
    b=n+4
    print(str(a)+","+str(b),end=",")
    n=b
    a=b
    
    
    
