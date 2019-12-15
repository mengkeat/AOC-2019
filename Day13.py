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

def break_blocks():
    input, paddle_x = [], 0
    c = list(code)
    c[0] = 2
    prog = Intcode(c, input)

    try:
        while True:
            x, y, z = next(prog), next(prog), next(prog)
            if (x,y)==(-1,0):
                print(z, end=' ')
            paddle_x =  x if z==PADDLE else paddle_x
            if z==BALL:
                input.append((x>paddle_x)-(x<paddle_x))
    except StopIteration:
        print("End of gameplay")

print("Part 2:")
break_blocks()