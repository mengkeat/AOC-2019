from collections import defaultdict
from functools import *
from itertools import *
from heapq import *

rawdat = [x.strip('\n') for x in open("Day20.txt").readlines()]
labels = defaultdict(list)
def get(r1, c1, r2, c2, r, c):
    raw = rawdat[r+r1][c+c1]+rawdat[r+r2][c+c2]
    return raw if raw.isalpha() else None
is_outer = lambda r, c: r in (2, len(rawdat)-3) or c in (2, len(rawdat[0])-3)

D = [(-2,0,-1,0), (1,0,2,0), (0,-2,0,-1), (0,1,0,2)]
for r in range(2, len(rawdat)-2):
    for c in range(2, len(rawdat[0])-2):
        lbl = reduce(lambda x, y: x or y, [get(*d, r, c) for d in D], None)
        if rawdat[r][c] == '.' and lbl:
            labels[lbl].append((r,c))
JMP = dict( [v for k,v in labels.items() if k not in ('AA', 'ZZ')] + \
            [v[::-1] for k,v in labels.items() if k not in ('AA', 'ZZ')] )

def do_jump(r, c, l, levels):
    if (r,c) not in JMP: return []
    if levels and l==0 and is_outer(r,c): return []
    new_l = l if not levels else (l-1 if is_outer(r,c) else l+1)
    return  [ (*JMP[(r,c)], new_l) ]

ED = [(0,1), (0,-1), (1,0), (-1,0)]
def get_steps(start, end, levels=False):
    V, Q = set(), [(0, *start)]
    while Q:
        d, r, c, l = heappop(Q)
        if (r, c, l) == end: return d
        V.add((r,c,l))
        cand = [(r+dr, c+dc, l) for dr,dc in ED] + do_jump(r, c, l, levels)
        for pr, pc, pl in cand:
            if rawdat[pr][pc]=='.' and (pr, pc, pl) not in V:
                heappush(Q, (d+1, pr, pc, pl))

start, end  = (*labels['AA'][0], 0), (*labels['ZZ'][0], 0)
print(f"Part 1: {get_steps(start, end)}")

print(f"Part 2: {get_steps(start, end, True)}")