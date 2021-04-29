
set1 = {1,2,(3,4)} #set can't contain list as lists are mutable

print(set1)

a = [1,2,3,4]
b = set(a)
print(b)

c = tuple(a)
print(c)

d = list(c)
print(d)

e = {}
print(type(e))

f = set()
print(type(f))

set1.add(5)
print(set1)


set1.update(str(6), [7,8], tuple(['a', 'b']))
print(set1)

#{1, 2, 'a', 5, (3, 4), 7, 8, 'b', '6'}

set1.discard(1)
set1.discard('a')
set1.remove(5)
print(set1)
#set1.remove(9) will through error

set1.pop()
print(set1)

set1.clear()
print(set1)

s1 = {1,2,3,4}
s2 = {3,4,7,8}

print('union', s1 | s2)
print('union', s1.union(s2))
print('union', s2.union(s1))
print('intersection', s1 & s2)
print('symmetric difference', s1 ^ s2)
print('symmetric difference', s1.symmetric_difference(s2))
print('symmetric difference', s2.symmetric_difference(s1))
print('intersection', s1.intersection(s2))
print('intersection', s2.intersection(s1))
print('s1 - s2', s1 - s2)
print('s2 - s1', s2 - s1)



