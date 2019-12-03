import os
from functools import reduce

with open("Day01.txt") as f:
    dat_str = f.readlines()
    dat = [int(x.strip()) for x in dat_str]

# Part 1
dat1 = map(lambda x: x//3-2, dat)
sum1 = reduce(lambda a,b: a+b, dat1)
print(f"Part 1 sum: {sum1}")

# Part 2
def iterative_fuel(x):
    a, s = x, 0
    while a>0:
        a = a//3 - 2
        s += (a if a>0 else 0)
    return s

sum2 = reduce(lambda a,b: a+b, map(iterative_fuel, dat))
print(f"Part 2 sum: {sum2}")