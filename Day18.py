from functools import *

m = [x.strip() for x in open("Day18.txt").readlines()]
NR, NC = len(m), len(m[0])
KEYS = [chr(x) for x in range(ord('a'), ord('z'))]
DOORS = [x.upper() for x in KEYS]
NODES = KEYS + DOORS
pos_map = dict([(m[r][c] ,(r,c)) for r in range(NR) for c in range(NC) if m[r][c] in NODES])

@lru_cache(maxsize=None)
def get_neighbours(node):
    pass