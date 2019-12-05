with open("Day05.txt") as infile:
    dat = [int(x) for x in infile.readline().strip().split(",")]

def decode(instr):
    opcode = instr % 100
    first = (instr//100) % 10
    second = (instr//1000) % 10
    return opcode, first==0, second==0

def Intcode(prog, inp=1, part2 = False):
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
            s[s[c+1]] = inp
            c += 2
        elif instr==4:
            print(f"val: {s[s[c+1]]}")
            c += 2
        elif part2 and instr==5:
            first, second = load(s[c+1], a), load(s[c+2], b)
            c = second if first!=0 else c+3
        elif part2 and instr==6:
            first, second = load(s[c+1], a), load(s[c+2], b)
            c = second if first==0 else c+3
        elif part2 and instr==7:
            first, second, third = load(s[c+1], a), load(s[c+2], b), s[c+3]
            s[third] = 1 if first < second else 0
            c += 4
        elif part2 and instr==8:
            first, second, third = load(s[c+1], a), load(s[c+2], b), s[c+3]
            s[third] = 1 if first==second else 0
            c += 4
        else:
            print(f"Invalid opcode {instr} {s[c]} pos: {c}")
            return


print(f"Part 1:")
Intcode(dat)
print(f"\nPart 2:")
Intcode(dat, 5, True)
