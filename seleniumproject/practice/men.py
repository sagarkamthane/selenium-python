import constant
print(constant.GRAVITY, constant.PI, constant.planet)
constant.PI = 3
print(constant.PI)

string = "sagar.txt is boy"
char = "s"

cars = ['tata', 'suzuki', 'kia', 'audi' ]  # list
bikes = ('honda', 'hero', 'yamaha') #tuple
family = {"sagar.txt" : "son", "sadhana" : "daughter", "pratibha" : "wife", "sanjeev" : "father"}
fam = {'sanjeev', 'sadhana', 'pratibha', 'sagar.txt'}

a = 5
print(type(a))
print(isinstance(5,int))

com = 1 + 2j
print(com,"\n", com.imag,"\n", com.real)

def tn(a,b):
    return a+b, a-b

print(tn(4,5))