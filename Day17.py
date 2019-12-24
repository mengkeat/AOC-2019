from intcode import *
from collections import defaultdict
from itertools import *
import re

code = [int(x) for x in open("Day17.txt").readline().strip().split(",")]+[0]*10000

SF, SP, EOL = 35, 46, 10

def getmap2(code, input=[]):
    prog = Intcode(code, input)
    arr = "".join([chr(x) for x in prog]).split(chr(10))
    m_str = [e for e in  arr if len(e)>1]
    d, NR, NC = defaultdict(int), len(m_str), len(m_str[0])
    m_ord = [ord(x) for x in "".join(m_str)]
    for coord, e in zip( [(r,c) for r in range(NR) for c in range(NC)], m_ord):
        d[coord] = e
    return d, NR, NC, ord(arr[-1]) if len(arr[-1])==1 else None

def alignment(m, nr, nc):
    is_inter = lambda r, c: m[(r,c)]==SF and m[(r+1,c)]==SF and m[(r-1,c)]==SF and m[(r,c+1)]==SF and m[(r,c-1)]==SF
    s =[r*c for r in range(1, nr-1) for c in range(1, nc-1) if is_inter(r,c)]
    return sum(s)

ship_map, NR, NC, _ = getmap2(list(code))

def draw_map():
    for r in range(NR):
        for c in range(NC):
            print(chr(ship_map[(r,c)]), end='')
        print()
draw_map()
print(f"Part 1: {alignment(ship_map, NR, NC)}")

N, S, E, W = range(4)
L = [(0,-1), (0,1), (-1,0), (1,0)]
R = [(0,1), (0,-1), (1,0), (-1,0)]
start_pos = [p for p, t in ship_map.items() if t==ord('^')][0]

is_SF_rel = lambda p, v: ship_map[(p[0]+v[0], p[1]+v[1])] == SF

def trace(pos, vec, dir, count):
    if is_SF_rel(pos, vec):
        return trace((pos[0]+vec[0], pos[1]+vec[1]), vec, dir, count+1)
    elif is_SF_rel(pos, L[dir]):
        return [str(count), 'L'] + trace(pos, L[dir], [W,E,N,S][dir], 0)
    elif is_SF_rel(pos, R[dir]):
        return [str(count), 'R'] + trace(pos, R[dir], [E,W,S,N][dir], 0)
    else:
        return [str(count)]

path = trace(start_pos, (-1,0), N, 0)
if path[0]=='0':
    path = path[1:]
print(f"Full path: {path}")

p2s = lambda p: "".join([str(x) for x in p])
s2p = lambda s: list(chain(*re.findall('(R|L)(\d+)', s)))
p2inp  = lambda p: [ord(x) for x in ",".join(p)]+[EOL]
   
def extract_path(orig_path, sub_path):
    return set([tuple(s2p(x)) for x in p2s(orig_path).split(p2s(sub_path)) if len(x)])

def decompose_path():
    for i in range(4, len(path)//2, 2):
        A = path[:i]
        path2 = extract_path(path, A)
        cand_B = min(path2, key=lambda x: len(x))
        for j in range(2, len(cand_B)+1, 2):
            path3 = set(chain(*map(lambda p: extract_path(p, cand_B[:j]), path2)))
            if len(path3)!=1: continue
            B, C = cand_B[:j], list(path3)[0]
            if len(p2s(A))<=20 and len(p2s(B))<=20 and len(p2s(C))<=20:
                return A, B, C

A, B, C  = decompose_path()
routine = p2s(path).replace(p2s(A), "A").replace(p2s(B), "B").replace(p2s(C), "C")

def dust():
    input = p2inp(routine)+p2inp(A)+p2inp(B)+p2inp(C)+[N, EOL]
    c = list(code)
    c[0] = 2
    m, nr, nc, d = getmap2(c, input)
    return d

print(f"Part 2: {dust()}")