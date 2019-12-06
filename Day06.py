from functools import lru_cache
from itertools import dropwhile

with open("Day06.txt") as infile:
    dat = [x.strip().split(')') for x in infile.readlines()]
    adj_rev = dict([(x[1], x[0]) for x in dat])

@lru_cache(maxsize=None)
def count_orbit(node):
    return (0 if node=='COM' else count_orbit(adj_rev[node])+1)

p1 = sum(map(lambda n: count_orbit(n), adj_rev.keys()))
print(f"Part 1: {p1}")

ancestors = lambda n: ['COM'] if n=='COM' else [n]+ancestors(adj_rev[n])
you_set, san_set = ancestors("YOU"), ancestors("SAN")
common = next(dropwhile(lambda x: x not in you_set, san_set))

p2 = count_orbit("YOU")+count_orbit("SAN")-(count_orbit(common)*2)-2
print(f"Part 2: {p2}")