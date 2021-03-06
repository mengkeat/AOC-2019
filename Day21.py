from intcode import *

code = [int(x) for x in open("Day21.txt").readline().strip().split(",")]+[0]*100

damage = lambda inp: [x for x in Intcode(code, [ord(x) for x in inp])]
def output(out):
    for x in out:
        print(chr(x) if x<=127 else x, end='')    
    print()

Code1 = """
NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
WALK
""".lstrip()

print("Part 1:")
output(damage(Code1))

Code2 = """
NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
NOT E T
NOT T T 
OR H T
AND T J
RUN
""".lstrip()

print("\nPart 2:")
output(damage(Code2))