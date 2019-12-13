from intcode import *

with open("Day09.txt") as infile:
    dat = [int(x) for x in infile.readline().strip().split(",")]
    dat = dat + [0]*10000

TEST1 = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]+[0]*3000 
TEST2 = [1102,34915192,34915192,7,4,7,99,0]+[0]*3000 
TEST3 = [104,1125899906842624,99]+[0]*3000

boost = lambda prog, inputs: [x for x in Intcode(prog, inputs)]

assert boost(TEST1, [0])==[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
assert len(str((boost(TEST2, [0])[0])))==16
assert boost(TEST3, [0])[0]==1125899906842624
print(f"Part 1: {boost(dat, [1])}")

print(f"Part 2: {boost(dat, [2])}")