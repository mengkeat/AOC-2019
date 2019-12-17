from intcode import *
from collections import defaultdict
from itertools import *
import re

code = [int(x) for x in open("Day17.txt").readline().strip().split(",")]+[0]*10000

SF, SP, EOL = 35, 46, 10

def getmap():
    prog = Intcode(list(code), [])
    m, r, c = defaultdict(int), 0, 0
    NR, NC = 0, 0
    try:
        while True:
            e = next(prog)
            if e==EOL:
                r, c = r+1, 0
            else:
                m[(r,c)] = e
                c += 1
            NR, NC = max(NR, r), max(NC, c)
    except StopIteration:
        print("Program terminate")
    return m, NR, NC

def alignment(m, nr, nc):
    is_inter = lambda r, c: m[(r,c)]==SF and m[(r+1,c)]==SF and m[(r-1,c)]==SF and m[(r,c+1)]==SF and m[(r,c-1)]==SF
    s =[r*c for r in range(1, nr-1) for c in range(1, nc-1) if is_inter(r,c)]
    return sum(s)

ship_map, NR, NC = getmap()

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

def trace(pos):
    path, Dir, vec, count = [], N, (-1,0), 0
    is_SF_rel = lambda x, y: ship_map[(pos[0]+x, pos[1]+y)] == SF
    while True:
        if is_SF_rel(*vec):
            pos = (pos[0]+vec[0], pos[1]+vec[1])
            count += 1
        elif is_SF_rel(*L[Dir]):
            vec = L[Dir]
            Dir = [W, E, N, S][Dir]
            path += [count, 'L']
            count = 0
        elif is_SF_rel(*R[Dir]):
            vec = R[Dir]
            Dir = [E, W, S, N][Dir]
            path += [count, 'R']
            count = 0
        else:
            path += [count]
            return path[1:]

path = trace(start_pos)
print(f"Full path: {path}")
p2s = lambda p: "".join([str(x) for x in p])
s2p = lambda s: list(chain(*re.findall('(R|L)(\d+)', s)))
    
def extract_path(orig_path, sub_path):
    return set([tuple(s2p(x)) for x in p2s(orig_path).split(p2s(sub_path)) if len(x)])

def decompose_path():
    possible = []
    for i in range(4, len(path)//2, 2):
        A = path[:i]
        path2 = extract_path(path, A)
        # for x in path2:
        #     print(p2s(A), p2s(x))
        cand_B = min(path2, key=lambda x: len(x))
        # print(f"B: {p2s(cand_B)} {len(cand_B)}")
        if len(A)>20 or len(cand_B)>20: 
            continue
        for j in range(2, len(cand_B)+1, 2):
            path3 = list(set(chain(*map(lambda p: extract_path(p, cand_B[:j]), path2))))
            # print([p2s(x) for x in path3])
            if len(path3)!=1:
                continue
            B = cand_B[:j]
            C = path3[0]
            if len(B)<=20 and len(C)<=20:
                possible.append((A, B, C))
    return possible

cand  = decompose_path()

# Multiple possible solutions. Use only one of it
A, B, C = cand[0]
path_str = p2s(path)
As, Bs, Cs = p2s(A), p2s(B), p2s(C)
routine = path_str.replace(As, "A").replace(Bs, "B").replace(Cs, "C")
print(routine)
print(A)
print(B)
print(C)
print()

