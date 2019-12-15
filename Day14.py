import re, math
from collections import defaultdict

react = {}
with open("Day14.txt") as infile:
    for line in infile.readlines():
        items = [(e, int(c)) for c, e in re.findall("(\d+) (\w+)", line)]
        react[items[-1][0]] = [items[-1][1], dict(items[:-1])]

def get_min_ore(num_fuel = 1):
    ore_count, inventory = 0, defaultdict(int)
    curr = {'FUEL': num_fuel}
    while True:
        prod = defaultdict(int)
        for k,v in curr.items():
            units = math.ceil(v/react[k][0])
            for ele, num in react[k][1].items():
                prod[ele] += num * units
            inventory[k] += (units * react[k][0] - v)

        if len(prod)==1 and "ORE" in prod:
            return ore_count+prod["ORE"]
        ore_count += prod["ORE"]

        curr = {}
        for k,v in prod.items():
            if k=="ORE": continue
            curr[k] = max(v-inventory[k], 0)
            inventory[k] = max(inventory[k]-v, 0)
print(f"Part 1: {get_min_ore()}")

# Finds maximum amount of fuel for num_ores
num_ores = 1000000000000
a, b = 1, num_ores
while a<b:
    mid = a + (b-a)//2
    if get_min_ore(mid) <= num_ores:
        a = mid+1
    else: 
        b = mid-1
print(f"Part 2: {a} {get_min_ore(a-1)} {get_min_ore(a)} {get_min_ore(a+1)}")