from functools import *
from itertools import *
import heapq

m = [x.strip() for x in open("Day18-test2.txt").readlines()]
NR, NC = len(m), len(m[0])
KEYS = [chr(x) for x in range(ord('a'), ord('z'))]
DOORS = [x.upper() for x in KEYS]
ALL_NODES = KEYS + DOORS + ['@']
DIR = [-1, 1, -1j, 1j] # N,S,E,W

POS_MAP = dict([(m[r][c] ,r+c*1j) for r in range(NR) for c in range(NC) if m[r][c] in ALL_NODES])
get_map = lambda p: m[int(p.real)][int(p.imag)]

@lru_cache(maxsize=None)
def neighbours(node):
    visited, s = set([POS_MAP[node]]), [(POS_MAP[node], 0)]
    neigh = []
    while len(s):
        p, d = s.pop()
        visited.add(p)
        cand = [p+di for di in DIR if (p+di) not in visited]
        for c in cand:
            if get_map(c)==".":
                s.append((c, d+1))
            elif get_map(c) in ALL_NODES:
                neigh.append((get_map(c), d+1))
    return dict(neigh)

from math import inf
shortest = dict( [(n2, dict([(n1, inf) for n1 in POS_MAP.keys()])) for n2 in POS_MAP.keys()] )
req_keys = dict( [(n2, dict([(n1, set()) for n1 in POS_MAP.keys()])) for n2 in POS_MAP.keys()])
for k in POS_MAP.keys():
    shortest[k][k] = 0
    for n_k in neighbours(k):
        shortest[k][n_k] = neighbours(k)[n_k]
        if n_k in DOORS:
            req_keys[k][n_k].add(n_k.lower())
        if k in DOORS:
            req_keys[k][n_k].add(k.lower())
for k,i,j in product(POS_MAP.keys(), repeat=3):
    if shortest[i][j] > shortest[i][k]+shortest[k][j]:
        shortest[i][j] = shortest[i][k]+shortest[k][j]
        req_keys[i][j] = req_keys[i][j].union(req_keys[i][k])
        req_keys[i][j] = req_keys[i][j].union(req_keys[k][j])

print(shortest)
print(req_keys)

def can_access(start, end, keys):
    keys_required = req_keys[start][end]
    return all([k in keys_required for k in keys])