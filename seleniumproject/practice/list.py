
l = ['a', 1, 'b', 'cd', 's s k', 2.3]
print("lst", l)
print("index", l[2])
print("slicing",l[3:])
print(l[:3])
print(l[:3] + l[3:])

l.append(3)
print("append", l)

l.insert(2,3)
print("insert", l)

l.extend([7, "eight", [9, "nine", 9.0]])
print("extend", l)

print(l + [10, 11])

l[5:] = []
print(l)

print(['s'] * 3)

l[2:2] = [2, 4]
print(l)

del l[3]
print(l)
del l[4:]
print(l)

l.remove('a')
print(l)
l.pop(1)
print(l)
l.pop()
print(l)
l.clear()
print(l)

for x in range(10):
    l.append(2 ** x)

print(l)

p = [x ** 2 for x in range(10)]
print(p)

p.remove(4)

s = list('12345')
print(s)
print(type(s))

li = [1,2,3]
o,t = li[:2]
tr = li[2]
print(o, t, tr)




