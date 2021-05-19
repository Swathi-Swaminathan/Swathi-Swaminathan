#python program to print series: 36, 34, 30, 28, 24, ..
n=int(input())
print(n,end=",")
for i in range(n):
    a=n-2
    b=n-6
    print(str(a)+","+str(b),end=",")
    n=b
    a=b
