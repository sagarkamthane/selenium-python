
fil = open('sagar.txt', mode = 'r+', encoding= 'UTF-8')
fil.write('sagar sanjeev kamthane')
fil.close()

try:
    fil = open('sagar.txt', mode='r', encoding='UTF-8')
    print(fil.read())
finally:
    fil.close()

with open('sagar.txt', 'r') as fil:
    print(fil.read())

fil = open('sagar.txt', mode = 'r', encoding= 'UTF-8')
print(fil.read(6))
print(fil.read(8))
print(fil.tell())
fil.seek(0)
print(fil.read())

with open('sagar.txt', 'a') as fil:
    fil.write('\nsagar is an IT engineer.\n He is very talented person')

with open('sagar.txt' , 'r') as fil:
    for f in fil.read():
        print(f, end='')
    fil.seek(0)
    print('\n',fil.readline())
    print(fil.readlines())

with open('sagar.txt', 'w') as fil:
    fil.truncate()


import os
print(os.getcwd())

