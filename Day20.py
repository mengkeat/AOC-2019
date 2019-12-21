from collections import defaultdict
from functools import *
from itertools import *

rawdat = [x.strip('\n') for x in open("Day20.txt").readlines()]
labels = defaultdict(list)
def get(r1, c1, r2, c2, r, c):
    raw = rawdat[r+r1][c+c1]+rawdat[r+r2][c+c2]
    return raw if raw.isalpha() else None
NR, NC = len(rawdat), len(rawdat[0])
print(f"Rows: {NR} Cols: {NC}")

D = [(-2,0,-1,0), (1,0,2,0), (0,-2,0,-1), (0,1,0,2)]
for r in range(2, NR-2):
    for c in range(2, NC-2):
        lbl = reduce(lambda x, y: x or y, [get(*d, r, c) for d in D], None)
        if rawdat[r][c] == '.' and lbl:
            labels[lbl].append((r,c))
# [print(k,v) for k,v in labels.items()]