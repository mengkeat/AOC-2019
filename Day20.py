from collections import defaultdict
from functools import *
from itertools import *
from heapq import *

rawdat = [x.strip('\n') for x in open("Day20.txt").readlines()]
labels = defaultdict(list)
def get(r1, c1, r2, c2, r, c):
    raw = rawdat[r+r1][c+c1]+rawdat[r+r2][c+c2]
    return raw if raw.isalpha() else None

D = [(-2,0,-1,0), (1,0,2,0), (0,-2,0,-1), (0,1,0,2)]
for r in range(2, len(rawdat)-2):
    for c in range(2, len(rawdat[0])-2):
        lbl = reduce(lambda x, y: x or y, [get(*d, r, c) for d in D], None)
        if rawdat[r][c] == '.' and lbl:
            labels[lbl].append((r,c))
JMP = dict( [v for k,v in labels.items() if k not in ('AA', 'ZZ')] + \
            [v[::-1] for k,v in labels.items() if k not in ('AA', 'ZZ')] )

D = [(0,1), (0,-1), (1,0), (-1,0)]
def get_steps(start, end):
    V, Q = set(), [(0, start)]
    while Q:
        d, coord = heappop(Q)
        if coord == end: return d
        V.add(coord)
        cand = [(coord[0]+dx, coord[1]+dy) for dx,dy in D] + ([JMP[coord]] if coord in JMP else [])
        for p in cand:
            if rawdat[p[0]][p[1]]=='.' and p not in V:
                heappush(Q, (d+1, p))

print(f"Part 1: {get_steps(labels['AA'][0], labels['ZZ'][0])}")