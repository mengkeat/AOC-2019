from intcode import *

code = [int(x) for x in open("Day17.txt").readline().strip().split(",")]+[0]*10000

SF, SP, NL = 35, 46, 10

def getmap():
    prog = Intcode(list(code), [])
    m, curr = [], ""
    try:
        while True:
            e = next(prog)
            if e==NL:
                m.append(curr)
                curr =""
            else:
                curr += chr(e)
    except StopIteration:
        print("Program terminate")
    return m[:-1]

def alignment(m):
    is_inter = lambda r, c: m[r][c]=="#" and m[r+1][c]=="#" and m[r-1][c]=="#" and m[r][c+1]=="#" and m[r][c-1]=="#"
    s =[r*c for r in range(1, len(m)-1) for c in range(1, len(m[0])-1) if is_inter(r,c)]
    return sum(s)

ship_map = getmap()
for x in ship_map: print(x)
print(f"Part 1: {alignment(ship_map)}")