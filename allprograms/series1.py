#python program to print series: 7, 10, 8, 11, 9, 12, ... 
n=int(input())
print(n,end=",")
for i in range(n):
    a=n+3
    b=n+1
    print(str(a)+","+str(b),end=",")
    n=b
    a=b
