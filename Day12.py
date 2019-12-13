import re
from itertools import permutations

with open("Day12.txt") as infile:
    lines = infile.readlines()
    pos = [re.findall("(\d+|-\d+)", l) for l in lines]
    moon_dat = [ [int(x) for x in p]+[0,0,0] for p in pos ]

def simulate(moons, steps):
    def update_vel():
        for m1, m2 in permutations(moons, 2):
            c1_dv = [ (c2>c1)-(c2<c1) for c1, c2 in zip(m1[:3], m2[:3])]
            m1[3:] = [ d+v for d, v in zip(c1_dv, m1[3:]) ]

    def update_pos():
        for m in moons:
            m[:3] = [ p+v for p,v in zip(m[:3], m[3:])]

    for s in range(steps):
        update_vel()
        update_pos()
    return moons

energy = lambda moons: sum([ sum(map(abs, m[:3]))*sum(map(abs, m[3:])) for m in moons])

TEST_MOONS = [[-1,0,2,0,0,0], [2,-10,-7,0,0,0], [4,-8,8,0,0,0], [3,5,-1,0,0,0]]
assert energy(simulate(TEST_MOONS, 10))==179
print(f"Part 1: {energy(simulate(moon_dat, 1000))}")
