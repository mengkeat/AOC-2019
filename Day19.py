from intcode import *
from functools import *
from itertools import *

code = [int(x) for x in open("Day19.txt").readline().strip().split(",")]+[0]*100
beam = lambda x, y: next(Intcode(list(code), [x,y]))

tractor_50 = [beam(x,y) for y,x in product(range(50), repeat=2)]
print(f"Part 1: {sum(tractor_50)}")

def contact(row):
    x, y = int(row*1.5), row
    while not beam(x,y): x += 1
    return x,y

lo, hi = 1, 1000
while lo<hi:
    mid = (lo+hi)//2
    x, y = contact(mid)
    if not beam(x+99,y-99):
        lo = mid+1
    else:
        hi = mid-1

x, y = contact(lo+1)
x1, y1 = x+99, y-99
print(f"Part 2: {x*10000+y1}")

