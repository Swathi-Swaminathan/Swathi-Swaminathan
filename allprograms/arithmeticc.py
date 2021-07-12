a = int(input("Enter a number:"))


def square():
    global a
    print("Square is=", a * a)


def cube():
    global a
    print("Cube is=", a * a * a)


def fact():
    global a
    f = 1
    for i in range(1, a + 1):
        f = f * i
    print("Factorial is=", f)


def sos():
    global a
    sum = 0
    for i in range(1, a + 1):
        sum = sum + i
    print("sum of series is=", sum)


sos()
square()
cube()
fact()
