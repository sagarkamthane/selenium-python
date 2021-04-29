for k in range(4):
    for l in range(k+1):
        print("*", end="")
    print("")

for i in range(4):
    for j in range(4-i, 0, -1):
        print("*", end= "")
    print("")

for x in range(4) :
    for y in range(4-x-1, 0, -1):
        print(" ", end = "")
    for z in range(x+1):
        print("*", end = "")
    print("")

for i in range(4):
    for j in range(i):
        print(" ", end="")
    for k in range(4-i, 0, -1):
        print("*", end = "")
    print("")

x = int(input("enter a no"))
for i in range(x):
    for j in range(x-i-1, 0, -1):
        print("    ", end="")
    for k in range(i*2+1):
        print("Neha",end="")
    print("")
for i in range(x-1):
    for j in range(i+1):
        print("    ", end="")
    for k in range((x-1)*2-2*i-1):
        print("Neha", end="")
    print("")