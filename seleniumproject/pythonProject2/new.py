a=3
print(a)

hi = "hi"
print(hi)

a, b, c = 5, 10, "sagar"

print(a, b, c)

print("{} {} {}".format("Im", a, "years old"))

#list
values = [1, 2, 3, "four", 5, 6.1 ]

print(values[0:5])

values.insert(5, "six")

values.append(7)

values[1] = "two "

values.remove(6.1)

del values[5]

print(values)

#tuple
val = (1, 2, 3, "four", '!' )

print(val.count(5))

#dictionary

dic = {1: "one", "two": 2}

print(dic[1])
print(dic["two"])

dict = {}

dict[1] = "one"
dict["two"] = 2

print(dict)

#if block

if dict[1] == "two":
     print("fail")
elif dict[1] == "on":
    print("PASS")
else:
    print("\nfail")

#for block
new = [1,2,3,4,5]
for i in new:
    print(i)

summ = 0
for j in range(1,6):
    summ = summ + j
    print(summ)


summ = 0
for j in range(1, 10, 2):
    summ = summ + j
    print(summ)


s = 5
while s > 0 :
    if s == 5:
        print(s)
        break
    print(s)
    s = s - 1

#function

def add(a, b):
    return a+b

print(add(5,6))

#class
print("latest")

class calculator:

    num = 100

    def __init__(self, a, b):
        self.fn = a
        self.sn = b

    def summ(self):
        return self.fn + self.sn

obj = calculator(2, 3)
print(obj.summ())


