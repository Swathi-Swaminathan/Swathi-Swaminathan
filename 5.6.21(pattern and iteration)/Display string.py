#Python program to display string in right angle triangle
str=input("Enter the name:")
b=len(str)
for i in range(b):
    for j in range(i+1):
        print(str[j],end="")
    print()
