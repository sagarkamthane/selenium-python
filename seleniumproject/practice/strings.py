string = 'sagar.txt'
print(string)
string = "sagar.txt"
print(string)
string = '''s
a
gar'''
print(string)
string = """s
ag
ar"""
print(string)

string = "sagar.txt is an IT engineer"
print(string[4])
print(string[:5])
print(string[5:])
print(string[-1])

string = ''
print(string)
del string

str1 = 'hello, '
str2 = 'sagar.txt'
print(str1 + str2 + '!')
lols = ('lol'*3)
count = 0
for lol in lols:
    if (lol == 'l'):
        count += 1

print('count of l is', count, end = ',' 'thakyou!\n')

print(lols.index('l'))
print(lols.count('l'))
print('l' in lols)

print(len(lols))



