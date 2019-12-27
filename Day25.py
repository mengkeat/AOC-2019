from intcode import *
from itertools import *
import re

code, inp = [int(x) for x in open("Day25.txt").readline().strip().split(",")]+[0]*100000, []
prog = Intcode(code, inp)

path = [
'north',
'take mutex',
'east',
'east',
'east',
'take whirled peas',
'west',
'west',
'west',
'south',
'west',
'take space law space brochure',
'north',
'take loom',
'south',
'south',
'take hologram',
'west',
'take manifold',
'east',
'north',
'east',
'south',
'take cake',
'west',
'south',
'take easter egg',
'south',
'south',
'inv',
]

items = ['mutex', 'whirled peas', 'space law space brochure', 'loom', 'hologram', 'manifold', 'cake', 'easter egg']

def next_input(silent=False):
    try:
        s = ""
        x = next(prog)
        while x != "GET":
            if silent:
                s += chr(x)
            else:
                print(chr(x), end='')
            x = next(prog)
        return s
    except StopIteration:
        print("Final: ")
        print(s)
 
def send(cmd, silent=False):
    print(cmd)
    i = [ord(x) for x in list(cmd)] + [10]
    inp.extend(i)
    return next_input(silent)
 
cmd_items = lambda items, s: [send(f"{s} {i}") for i in items]
take_items = lambda items: cmd_items(items, "take")
drop_items = lambda items: cmd_items(items, "drop")

next_input()
while path:
    send(path.pop(0))
drop_items(items)

item_combs = chain(*[combinations(items, i) for i in range(1, 9)])
for comb in item_combs:
    print(comb)
    take_items(comb)
    res = send("south")
    found = len(re.findall("(heavier|lighter)", res))==0
    drop_items(comb)
