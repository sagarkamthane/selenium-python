from new import calculator

class calcu(calculator) :
    numm = 120
    def __init__(self):
        calculator.__init__(self, 5, 10)


    def summm(self):
        return self.summ() + self.numm

obj = calcu()
print(obj.summm())

str1 = "    sagarsanjeevkamthane    ."
str2 = "sagar"

print(str1[0:5])
print(str1 + str2)
print(str1 in str2)

var = str1.split('s')
print(var)

print(str1.rstrip())
