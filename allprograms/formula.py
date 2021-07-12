def formula(a,b):
    return add(a,b) * add(a,b)
def add(a,b):
    return a+b
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))
print(formula(a,b))
