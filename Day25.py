from intcode import *

code, inp = [int(x) for x in open("Day25.txt").readline().strip().split(",")]+[0]*10000, []
prog = Intcode(code, inp)

while True:
    x = next(prog)
    while x != "GET":
        print(chr(x), end='')
        x = next(prog)
    i = [ord(x) for x in list(input())] + [10]
    inp.extend(i)