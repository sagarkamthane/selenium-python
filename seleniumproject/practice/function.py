def greet(name = "sagar.txt"):
    '''prints your name'''
    print(f"hello,{name}")

greet('sagar.txt')
print(greet.__doc__)

greet()

def evenorodd(num):
    if num% 2 == 1:
        return "odd"
    else:
        return "even"

print(evenorodd(3))

y = 20
def scope():
    x = 10
    print("x local inside function ",x)
    print("y global inside function ",y)

scope()

#def info(name = "sagar.txt", age): #invalid syntax

def sayhello(*names):
    for name in names:
        print("hi", name)

ls = ['sagar.txt', "sam", "ram", "pam"]
sayhello(*ls)


def factorial(n):
    if n > 2:                   #5, 4,
        n = n * factorial(n-1)  #5*fact(4), 5*4*fact(3),
    else:
        n = 1
    return n

print(factorial(5))

n = 12345

import sys
sys.setrecursionlimit(10**6)

def sum_n(n):

    if n > 0:
        n = n + sum_n(n-1)
    return n

print(sum_n(10000))


#lambda functions

double = lambda x: x*2

print(double(5))

#local global

x = 1
y = "global"
def fun():
    global y
    y = y + " world"
    z = "local"
    print(x)
    print(y)
    print(z)

fun()

x = 10
def gl():
    x = 5
    print(f"local x: {x}")

gl()
print("global x:",x)

print("------")
def outer():
    x = "local"
    print("outer x",x)
    z = 10

    def inner():
        nonlocal x
        global z
        z = 20
        x = "nonlocal"
        print("inner x",x)
        print("inner z",z)

    inner()
    print("outer x:",x)
    print("outer z", z)

outer()
print("main z", z)





