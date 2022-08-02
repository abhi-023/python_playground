def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
a = 12
def f():
    print('Inside f() : ', a)
def g():
    a = 22
    print('Inside g() : ', a)
def h():
    global a
    a = 23
    print('Inside h() : ', a)
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)