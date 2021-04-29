import prat.pratchild.pr
#from aexample import add,mul
#from aexample import *   --> not a good practice
#or
import aexample as e
#or
#import aexample
#e = aexample


print(e.add(5,10))
print(e.mul(2,5))

import sys
for a in sys.path:
    print(a)

import importlib as i
import aimp
i.reload(aimp)
import aimp

print(*dir(e))

print(e.__name__)

print(dir())

def tw(aa, bb):
    return aa+bb, bb-aa

print(tw(5,6))

