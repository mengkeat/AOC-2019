import os

with open("Day02.txt") as infile:
    actual_prog = [int(x) for x in infile.readline().strip().split(',')]

TEST1, ANS1 = [1,0,0,0,99], [2,0,0,0,99]
TEST2, ANS2 = [2,3,0,3,99], [2,3,0,6,99]
TEST3, ANS3 = [2,4,4,5,99,0], [2,4,4,5,99,9801]
TEST4, ANS4 = [1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99]

def Intcode(prog):
    state = list(prog)
    c = 0
    while state[c] != 99:
        instr, a, b, dest = state[c:c+4]
        if instr==1:
            state[dest] = state[a]+state[b]
        elif instr==2:
            state[dest] = state[a]*state[b]
        c+=4
    return state

assert Intcode(TEST1)==ANS1
assert Intcode(TEST2)==ANS2
assert Intcode(TEST3)==ANS3
assert Intcode(TEST4)==ANS4

# Part 1
actual_prog[1] = 12
actual_prog[2] = 2
print(Intcode(actual_prog))

# Part 2
DESIRED_OUTPUT = 19690720
for i in range(0, 100):
    for j in range(0, 100):
        actual_prog[1] = i
        actual_prog[2] = j
        output = Intcode(actual_prog)
        if output[0]==DESIRED_OUTPUT:
            print(f"{output[:3]}, Code: {output[1]*100+output[2]}")