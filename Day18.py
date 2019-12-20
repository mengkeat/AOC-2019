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
map_at = lambda p: m[int(p.real)][int(p.imag)]

def explore_fill(node):
    visited, s = set([POS_MAP[node]]), [(POS_MAP[node], 0, ())]
    connect = {}
    while len(s):
        p, d, k = s.pop()
        visited.add(p)
        curr_v = map_at(p)
        if curr_v in KEYS:
            connect[curr_v] = (d, k)
        cand = [p+di for di in DIR if (p+di) not in visited]
        for c in cand:
            if curr_v != '#':
                s.append( (c, d+1, k+(curr_v,) if curr_v in DOORS else k) )
    return connect
G = dict( [(n, explore_fill(n)) for n in POS_MAP.keys()] )

print(G)