from intcode import *
import heapq

with open("Day15.txt") as infile:
    code = [int(x) for x in infile.readline().strip().split(",")]

N,S,W,E = range(0, 4)
D = [(0,1), (0,-1), (-1,0), (1,0)]
REV = [S, N, E, W]
WALL, NORM, OXY = 0, 1, 2

input, prog = [], None
next_coord = lambda coord, dirn: (coord[0]+D[dirn][0], coord[1]+D[dirn][1])

def move_robot(cmd):
    global prog, input
    input.append(cmd+1)
    if prog is None:
        prog = Intcode(code, input)
    return next(prog)

def explore(grid):
    s, moves, coord = [], {}, (0,0)
    hist, visited = [], set() 

    while True:
        moves[coord] = [N,S,W,E] if coord not in moves else moves[coord]

        bt = False
        if moves[coord]:
            m = moves[coord].pop()
        else:
            bt = True
            m = REV[hist.pop()]
            if not hist: return grid

        nc = next_coord(coord, m)
        grid[nc] = move_robot(m)
        visited.add(nc)

        if grid[nc] != WALL:
            if not bt: hist.append(m)
            coord = nc

    return grid

def draw_grid(g):
    min_x, max_x = min(g.keys(), key=lambda x:x[0])[0], max(g.keys(), key=lambda x:x[0])[0]
    min_y, max_y = min(g.keys(), key=lambda x:x[1])[1], max(g.keys(), key=lambda x:x[1])[1]
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            print(g[(x,y)] if ((x,y) in g) and (g[(x,y)]!=NORM) else ' ', end='')
        print()

def shortest_and_fill(grid, dest, start=(0,0)):
    v, q = set(), [(0, start)]
    oxy_dist = None
    all_dist = []

    while q:
        dist, pos = heapq.heappop(q)
        if grid[pos] == OXY:
            oxy_dist = dist
        all_dist.extend([dist])
        v.add(pos)
        for dx, dy in D:
            npos = (pos[0]+dx, pos[1]+dy)
            if npos in grid and grid[npos]!=WALL and npos not in v:
                heapq.heappush(q, (dist+1, npos))

    return oxy_dist, max(all_dist)

g = {}
explore(g)
print(len(g))
draw_grid(g)
oxy_pos = [c for c,t in g.items() if t==OXY][0]

print(f"Part 1: {shortest_and_fill(g, oxy_pos)[0]}")
print(f"Part 2: {shortest_and_fill(g, oxy_pos, oxy_pos)[1]}")