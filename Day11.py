from intcode import *
from collections import defaultdict

with open("Day11.txt") as infile:
    code = [int(x) for x in infile.readline().strip().split(",")]+[0]*10000

U, D, L, R = (0,1), (0,-1), (-1,0), (1,0)
TURN_L = {U:L, L:D, D:R, R:U}
TURN_R = {U:R, R:D, D:L, L:U}

def paint(prog, start=0):
    x, y, d = 0, 0, U
    input = [start] 
    code = Intcode(prog, input)
    hull = defaultdict(int)

    try:
        while True:
            hull[(x,y)] = next(code)
            d = [TURN_L, TURN_R][next(code)][d]
            x, y = x+d[0], y+d[1]
            input.append(hull[(x,y)])
    except StopIteration:
        print("End of robot painting")
    return hull

hull_1 = paint(code)
print(f"Part 1: {len(hull_1)}")

def draw(h):
    xc, yc= zip(*h)
    min_x, max_x, min_y, max_y = min(xc), max(xc), min(yc), max(yc)
    for y in range(max_y, min_y-1, -1):
        for x in range(min_x, max_x+1):
            print('1' if h[(x,y)]==1 else ' ', end='')
        print()

hull_2 = paint(code, 1)
draw(hull_2)