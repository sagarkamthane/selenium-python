with open('txt.txt', 'r') as fileread:
    readl = fileread.readlines()
    print(readl)
    reversed(readl)
    with open('txt.txt', 'w') as filewrite:
        for line in reversed(readl):
            filewrite.write(line)

