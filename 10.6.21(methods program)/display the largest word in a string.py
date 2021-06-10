#Python program to display the largest word in a given string
string=input("Enter the string:")
largest=max(string.split(),key=len)
print("Largest word is:",largest)
