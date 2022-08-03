# labmda function
# Cube using lambda
n=int(input("enter the number"))
cube = lambda x: x * x * x
print(cube(n))
# List comprehension using lambda
a = [(lambda x: x * 2)(x) for x in range(5)]
print(a)