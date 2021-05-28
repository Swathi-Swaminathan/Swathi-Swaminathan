#python program to print sum of first largest and third smallest
n=[]
size=int(input("Enter the list size:"))
res=0

for i in range(size):
    x=int(input("Enter the elements"))
    n.append(x)

n.sort()
n.reverse()
print(n[0]+n[-3])
        
