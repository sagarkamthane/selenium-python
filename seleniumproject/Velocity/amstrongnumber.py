import math

a = int(input("enter a no"))
b = a
s = 0
power = len(str(a))

while a > 0:
    r = int(a % 10)
    s = s + pow(r, power)
    a = int(a / 10)

assert b == s
print(s)


