from intcode import *
from itertools import *

code = [int(x) for x in open("Day23.txt").readline().strip().split(',')]+[0]*10000

N = 50
S = [[] for _ in range(N)]
Q = dict( [(i, []) for i in range(N)] + [(255, list())] )
NIC = [Intcode(list(code), Q[i]) for i in range(N)]
for i, n in enumerate(NIC):
    next(n)
    Q[i].append(i)
    S[i] = next(n)

def step_nic(i):
    x, y  = None, None
    if not S[i]:
        S[i] = next(NIC[i])
    if  S[i] == "GET":
        if not Q[i]: Q[i].append(-1)
        a = S[i]
    else:
        x, y = next(NIC[i]), next(NIC[i])
        Q[S[i]].extend((x,y))
        a = S[i]
    S[i] = next(NIC[i])
    return a, x, y

is_idle = lambda: all(map(lambda x: len(x)==0, [Q[i] for i in range(N)]))
IDLE_LIMIT = 1000

def run_parts():
    part1 = False
    first, second = None, None
    idle_count = 0

    for i in cycle(range(N)):
        a, x, y = step_nic(i)
        if a != 255 and a != "GET":
            idle_count = 0

        if not part1 and Q[255]:
            print(f"Part 1: {Q[255][1]}")
            part1 = True

        if len(Q[255])>2:
            Q[255] = Q[255][-2:]
        if is_idle():
            idle_count += 1
            if idle_count == IDLE_LIMIT:
                Q[0].extend(Q[255][-2:])
                first, second = second, Q[255][1]
                if first is not None and first==second:
                    print(f"Part 2: {first}")
                    return first
                idle_count = 0

run_parts()