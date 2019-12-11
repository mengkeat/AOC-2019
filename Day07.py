from itertools import permutations
from functools import reduce 

with open("Day07.txt") as infile:
    dat = [int(x) for x in infile.readline().strip().split(",")]

decode = lambda instr: (instr%100, (instr//100)%10==0, (instr//1000)%10==0)

def Intcode(prog, input=None):
    output = []
    s = list(prog)
    c = 0
    in_iter = iter(input)
    load = lambda v, ispos: s[v] if ispos else v

    while s[c] != 99:
        instr, a, b= decode(s[c])
        if instr==1:
            s[s[c+3]] = load(s[c+1], a) + load(s[c+2], b)
            c += 4
        elif instr==2:
            s[s[c+3]] = load(s[c+1], a) * load(s[c+2], b)
            c += 4
        elif instr==3:
            s[s[c+1]] = next(in_iter)
            c += 2
        elif instr==4:
            # print(f"val: {s[s[c+1]]}")
            output.append(s[s[c+1]])
            c += 2
        elif instr==5:
            first, second = load(s[c+1], a), load(s[c+2], b)
            c = second if first!=0 else c+3
        elif instr==6:
            first, second = load(s[c+1], a), load(s[c+2], b)
            c = second if first==0 else c+3
        elif instr==7:
            first, second, third = load(s[c+1], a), load(s[c+2], b), s[c+3]
            s[third] = 1 if first < second else 0
            c += 4
        elif instr==8:
            first, second, third = load(s[c+1], a), load(s[c+2], b), s[c+3]
            s[third] = 1 if first==second else 0
            c += 4
        else:
            print(f"Invalid opcode {instr} {s[c]} pos: {c}")
            break
    return output[-1]

run_phase = lambda prog, phase_seq: reduce(lambda acc, x: Intcode(prog, [x, acc]), phase_seq, 0)
get_max = lambda p: max(map(lambda x: run_phase(p, x), permutations(range(0,5))))

test1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
test2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
        101,5,23,23,1,24,23,23,4,23,99,0,0]
test3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
        1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

assert get_max(test1)==43210
assert get_max(test2)==54321
assert get_max(test3)==65210

print(f"Part 1: {get_max(dat)}")
