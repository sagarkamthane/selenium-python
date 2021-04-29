
values = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4  }
val1 = dict({'a': 1, 'b': 2})
val2 = dict([('a', 1),('b', 2)])
print(values)
print(val1)
print(val2)
print(values['a'])
print(values.get('b'))
values['e'] = 5
print(values)

values.pop('c')
print(values)
values.popitem()
print(values)
values.clear()
print(values)

del values
#print(values)  throws error

dict = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4  }

for key,val in dict.items():
    if val == 2:
        print(key)
