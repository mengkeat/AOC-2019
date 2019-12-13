from intcode import *

with open("Day13.txt") as infile:
    code = [int(x) for x in infile.readline().strip().split(",")]+[0]*10000

EMPTY, WALL, BLOCK, PADDLE, BALL = range(5)

def draw_tiles(code):
    prog = Intcode(code, [])
    grid = {}
    try:
        while True:
            x, y, z = next(prog), next(prog), next(prog)
            grid[(x,y)] = z
    except StopIteration:
        print("End drawing")
    return grid

p1 = len([x for x in draw_tiles(list(code)).values() if x==BLOCK])
print(f"Part 1: {p1}")
