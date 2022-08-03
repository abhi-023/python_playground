# A simple Python function
def fun():
    print("Welcome to Aarth")
# Driver code to call a function
fun()
# some more functions
n = int(input("enter the number"))
def is_prime(n):
    if n is [2,3]:
        return True
    if (n%2==0):
        return False
    r = 3
    while r*r<=n:
        if (n%r==0):
            return False
        r+=2
    return True
print(is_prime(n))
# arguments
# default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
myFun(10)
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
# Keyword arguments
student(firstname='Abhiram', lastname='Moturi')
student(lastname='Codes', firstname='Python')
# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)
myFun('Hello', 'Welcome', 'to', 'AarthSoftware')
# Python program to illustrate
# *kwargs for variable number of keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun(first='Abhi', mid='ram', last='Moturi')
