#Python program to display the first and last letter in a string in capital letters
a=input("Enter the String:")
a1=a.title()
w=a1.split()
r=""
for i in w:
    r=r+i[:-1]+i[-1].upper()+" "
print("New string:",r[:-1])

