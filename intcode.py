decode = lambda instr: (instr%100, (instr//100)%10, (instr//1000)%10, (instr//10000)%10)

def Intcode(prog, input):
    output = []
    s = list(prog)
    pc = 0
    rel_base = 0
    index = lambda pos, mode: {0: s[pos], 1: pos, 2: s[pos]+rel_base }[mode]
    load = lambda pos, mode: s[index(pos, mode)]

    while s[pc] != 99:
        instr, a, b, c = decode(s[pc])
        if instr==1:
            s[index(pc+3, c)] = load(pc+1, a) + load(pc+2, b)
            pc += 4
        elif instr==2:
            s[index(pc+3, c)] = load(pc+1, a) * load(pc+2, b)
            pc += 4
        elif instr==3:
            if len(input)==0: 
                yield "GET"
            s[index(pc+1, a)] = input.pop(0) 
            pc += 2
        elif instr==4:
            yield load(pc+1, a)
            pc += 2
        elif instr==5:
            first, second = load(pc+1, a), load(pc+2, b)
            pc = second if first!=0 else pc+3
        elif instr==6:
            first, second = load(pc+1, a), load(pc+2, b)
            pc = second if first==0 else pc+3
        elif instr==7:
            first, second = load(pc+1, a), load(pc+2, b)
            s[index(pc+3, c)] = 1 if first < second else 0
            pc += 4
        elif instr==8:
            first, second = load(pc+1, a), load(pc+2, b)
            s[index(pc+3, c)] = 1 if first==second else 0
            pc += 4
        elif instr==9:
            rel_base += load(pc+1, a)
            pc += 2
        else:
            print(f"Invalid opcode {instr} {s[pc]} pos: {pc}")
            break

