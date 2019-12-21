from functools import *
from itertools import *
import heapq

m = [x.strip() for x in open("Day18.txt").readlines()]
NR, NC = len(m), len(m[0])
DIR = [-1, 1, -1j, 1j] # N,S,E,W

get_pos_map = lambda m: dict([(m[r][c] ,r+c*1j) for r in range(NR) for c in range(NC) 
                if m[r][c].islower() or m[r][c]=='@' or m[r][c] in ('1', '2', '3', '4')])

POS_MAP = get_pos_map(m)
NKEYS = len([x for x in POS_MAP if x.islower()])
map_at = lambda p: m[int(p.real)][int(p.imag)]

def explore_fill(node):
    visited, Q = set(), [(POS_MAP[node], 0, set())]
    connect = dict()
    while Q:
        p, d, k = Q.pop(0)
        visited.add(p)

        curr_v = map_at(p)
        if curr_v.islower():
            connect[curr_v] = (d, set(k))
        cand = [p+di for di in DIR if p+di not in visited]
        for c in cand:
            if map_at(c) != '#':
                Q.append( (c, d+1, k|set(map_at(c).lower()) if map_at(c).isupper() else k) )
    return connect

G = dict( [(n, explore_fill(n)) for n in POS_MAP.keys()] )

def shortest(G, start):
    Q = [(0, (start, frozenset())) ]
    shortest_dist = {}
    while Q:
        dist, (node, curr_keys) = heapq.heappop(Q)
        if (node, curr_keys) in shortest_dist: 
            continue
        shortest_dist[(node, curr_keys)] = dist
        if len(curr_keys)==NKEYS:
            return dist

        for i in range(len(node)):
            for next_node, (d_to_node, req_keys) in G[node[i]].items():
                if len(req_keys-curr_keys)==0 and next_node not in curr_keys:
                    new_keys = curr_keys|frozenset(next_node)
                    new_node = node[:i]+(next_node,)+node[i+1:]
                    heapq.heappush(Q, (dist+d_to_node, (new_node, new_keys)))

print(f"Part 1: {shortest(G, ('@',))}")

# Ugly but just redefine here
m = [x.strip() for x in open("Day18-2.txt").readlines()]
POS_MAP = get_pos_map(m)
G2 = dict( [(n, explore_fill(n)) for n in POS_MAP.keys()] )

print(f"Part 2: {shortest(G2, ('1', '2', '3', '4'))}")