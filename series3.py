#Python program to print series: 22, 21, 23, 22, 24, 23, ...
n=int(input())
print(n,end=",")
for i in range(n):
    a=n-1
    b=n+1
    print(str(a)+","+str(b),end=",")
    n=b
    a=b
