from itertools import permutations
from functools import reduce 

with open("Day07.txt") as infile:
    dat = [int(x) for x in infile.readline().strip().split(",")]

decode = lambda instr: (instr%100, (instr//100)%10==0, (instr//1000)%10==0)

def Intcode(prog, input=None):
    output = []
    s = list(prog)
    c = 0
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
            s[s[c+1]] = yield
            c += 2
        elif instr==4:
            yield s[s[c+1]]
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

send_phase = lambda amps, phase: list(map(lambda a, ph: a.send(ph), amps, phase))
def run_amps(amps, phase, init=0):
    try:
        send_phase(amps, phase)
        results =  reduce(lambda acc, x:  x.send(acc), amps, init)
    except StopIteration:
        return -1
    return results

def init_amps(p): 
    prog = [Intcode(p) for _ in range(5)]
    send_phase(prog, [None]*len(prog))
    return prog

get_max1 = lambda prog: max(map(lambda x: run_amps(init_amps(prog), x), permutations(range(0,5))))

test1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
test2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
        101,5,23,23,1,24,23,23,4,23,99,0,0]
test3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
        1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

assert get_max1(test1)==43210
assert get_max1(test2)==54321
assert get_max1(test3)==65210

print(f"Part 1: {get_max1(dat)}")

test4 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
        27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
test5 = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
        -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
        53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

def run_amps_iter(prog, phase):
    amps = init_amps(prog)
    init, out = 0, 0
    while out>=0:
        out = run_amps(amps, phase, init)
        init = out if out>0 else init
    return init
 
get_max2 = lambda prog: max(map(lambda phase: run_amps_iter(prog, phase), permutations(range(5,10))))
assert get_max2(test4)==139629729
assert get_max2(test5)==18216

print(f"Part 2: {get_max2(dat)}")