
try:
    with open('txtt.txt', 'r') as readerror:
        readerror.read()

except: #catch
    print("error in try")



try:
    with open('txtt.txt', 'r') as readerror:
        readerror.read()

except Exception as e: #prints error reason
    print(e)

finally:
    print("it is executed every time")