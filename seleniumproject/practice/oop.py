

class emp:
    company = 'google'
    def __init__(self, name, profile, salary, increment, address = "NA"):
        self.name = name
        self.profile = profile
        self.salary = salary
        self.increment = increment
        self.address = address

    def details(self):
        return f'{self.name} is {self.profile} at {self.company} and his salary is {self.salary}'

    def hike(self, newsal = int()):
        self.newsal = newsal
        print(self.newsal)
        if 'Engineer' in self.profile:
            self.salary += self.salary*self.increment/100
            return self.salary
        else:
            return 'No increment'

e1 = emp('sagar', 'QA Engineer', 50000, 15)
print(e1.details())
print(e1.hike())

e2 = emp('sagar', 'sw engineer', 100000, 15)
print(e2.details())
print(e2.hike())

e3 = emp('sagar', 'manager', 100000, 15)
print(e3.details())
print(e3.hike())


# Inheritance

class man:
    def __init__(self, name, age,  gender):
        self.name = name
        self.age = age
        self.gender = gender

    def function(self):
        print("can walk")

class stud(man):
    def __init__(self,name, age, marks , gender = ''):
        super().__init__(name, age, gender)
        self.marks = marks

    def studinfo(self):
        print(f'{self.name} is a {self.gender}, he is {self.age} years old and he has scored {self.marks} marks')

    def func(self):
        print("can study")

m1 = man('pandu', 70, 'Male')
m1.function()
s1 = stud('sagar', 23, 70, 'M')
s1.studinfo()
s1.function()
s1.func()

#salary calculator
class salary:

    def inp(self):
        self.currpkg, self.hikerate = int(input("Enter your current salary")), int(input('and hike rate in percentaged'))

    def __init__(self, currpkg = int(0), hikerate = int(0)):
        self.currpkg = currpkg
        self.hikerate = hikerate

    def calculate(self):
        total = 0
        for i in range(1, 11):
            self.currpkg = self.currpkg + self.currpkg*self.hikerate/100
            print(f'salary after {i} year: {self.currpkg}')
            total = total + self.currpkg
        print(total)

calc = salary()
calc.inp()
calc.calculate()

