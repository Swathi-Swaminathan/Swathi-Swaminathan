#Python program to display string in inverse right angle triangle
str=input("Enter the name:")
b=len(str)
for i in range(b):
    for j in range(b-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print(str[k],end=" ")
    print()
