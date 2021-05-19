#python program to print series: 53, 53, 40, 40, 27, 27, ...
n=int(input())
print(n,end=",")
for i in range(n):
    a=n
    b=n-13
    print(str(a)+","+str(b),end=",")
    n=b
    a=b
