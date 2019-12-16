from itertools import *
from functools import reduce

def convert_input(s):
    return [int(x) for x in s]

with open("Day16.txt") as infile:
    input = convert_input(infile.readline().strip())

base = [0, 1, 0, -1]
get_base = lambda pos, rep: base[(pos//rep)%4]

def FFT(inp, phase):
    for i in range(phase):
        out = [0] * len(inp)
        for j in range(1, len(inp)+1):
            c = sum( [get_base(count+1, j)*i for count, i in enumerate(inp)] )
            out[j-1] = (abs(c)%10)
        inp = out

    return ("".join([str(x) for x in inp]))[:8]

assert FFT(convert_input("80871224585914546619083218645595"),100) == "24176176"
assert FFT(convert_input("19617804207202209144916044189917"),100) == "73745418"
assert FFT(convert_input("69317163492948606335995924319873"),100) == "52432133"
print(f"Part 1: {FFT(convert_input(input), 100)}")

offset = lambda inp: reduce(lambda acc, x: acc*10+x, inp[:7])
print(f"Offset: {offset(input)} Len input: {len(input)} Len from offset: {len(input)*10000-offset(input)}")

def FFT2(inp, phase):
    L, off = len(inp), offset(inp)
    inp2 = [inp[x%L] for x in range(off, L*10000+1)][::-1]
    for _ in range(phase):
       inp2 = [x%10 for x in accumulate(inp2)]
    return "".join([str(x) for x in inp2[::-1][:8]])

assert FFT2(convert_input("03036732577212944063491565474664"),100) == "84462026"
assert FFT2(convert_input("02935109699940807407585447034323"),100) == "78725270"
assert FFT2(convert_input("03081770884921959731165446850517"),100) == "53553731"

print(f"Part 2: {FFT2(convert_input(input), 100)}")