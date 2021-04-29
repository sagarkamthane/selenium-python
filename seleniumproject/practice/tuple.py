tpl = ("s", 'a', 'g', 'a', 'r')
print(tpl)
print(tpl[2])
print(tpl[-2])
print(tpl[2:])
print(tpl[:2])
print(tpl.count('a'))

tp = tuple('1234')
print(tp)
print(type(tp[0]))

tpp = 1,2,3,4
print(tpp)
a,b,c,d = tpp
print(a,b,c,d)


tup = ("hello") #string
print(type(tup))
tup  = ('hello',) #tupple
print(type(tup))
tup = "hello", #tupple
print(type(tup))

mytup = ("sagar.txt", [1,2,3,4])
print(mytup[0][2])
print(mytup[1][2])
mytup[1].append(5)
print(mytup)
mytup[1][1] = 'two'
print(mytup)
mytup = ()
print(mytup)

t1 = (1,2,3,4)
t2 = ('five', 'six')
t3 = t1 + t2
print(t3)

t4 = (("hi",)*3)
print(t4)
del t4

print(2 in t3)
print('')

names = ('sagar.txt', 'om')
for name in names:
    print("hello " + name)