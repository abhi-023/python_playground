x=int(input("enter the number"))
y=int(input("enter the number"))
def add(x, y):
    return (x + y)
print(add(x, y))
add(x, y)
x=int(input("enter the number"))
y=int(input("enter the number"))
def sub(x, y):
    return (x - y)
print(sub(x, y))
# importing sqrt() and factorial from the
# module math
from math import *
print(sqrt(16))
print(factorial(6))
# locating module
# importing sys module
import sys
print(sys.path)
## renaming module
## importing sqrt() and factorial from the
## module math
import math as gfg
print(gfg.sqrt(16))
print(gfg.factorial(6))
# dir function
#  Import built-in module  random
import  random
print(dir(random))
