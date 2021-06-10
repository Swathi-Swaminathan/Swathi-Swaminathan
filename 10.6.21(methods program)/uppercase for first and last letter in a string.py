#Python program to display the first and last letter in a string in capital letters
a=input("Enter the String:")
a=a.title()
w=a.split()
r=""
for i in w:
    r=r+i[:-1]+i[-1].upper()+" "
print("New string:",r[:-1])

