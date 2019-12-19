from intcode import *
from functools import *
from itertools import *

code = [int(x) for x in open("Day19.txt").readline().strip().split(",")]+[0]*10000

tractor_50 = [next(a) for a in map(lambda x: Intcode(list(code), list(x)), product(range(50), repeat=2))]
print(f"Part 1: {sum(tractor_50)}")

for (x,y), a in zip(product(range(50), repeat=2), tractor_50):
    if y==0: print()
    print(a, end='')
