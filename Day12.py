import re
from itertools import *
from math import gcd

with open("Day12.txt") as infile:
    lines = infile.readlines()
    pos = [re.findall("(\d+|-\d+)", l) for l in lines]
    moon_dat = [ [int(x) for x in p]+[0,0,0] for p in pos ]

clone_moons = lambda moons: [list(x) for x in moons]

def update_vel(moons):
    """ Note: function destructive in parameter """
    for m1, m2 in permutations(moons, 2):
        c1_dv = [ (c2>c1)-(c2<c1) for c1, c2 in zip(m1[:3], m2[:3])]
        m1[3:] = [ d+v for d, v in zip(c1_dv, m1[3:]) ]
    return moons

def update_pos(moons):
    """ Note: function destructive in parameter """
    for m in moons:
        m[:3] = [ p+v for p,v in zip(m[:3], m[3:])]
    return moons

step = lambda moons: update_pos(update_vel(moons))
n_steps = lambda moons, n: list(starmap(step, repeat([moons], n)))[-1]
energy = lambda moons: sum([ sum(map(abs, m[:3]))*sum(map(abs, m[3:])) for m in moons])

TEST_MOONS = [[-1,0,2,0,0,0], [2,-10,-7,0,0,0], [4,-8,8,0,0,0], [3,5,-1,0,0,0]]
assert energy(n_steps(clone_moons(TEST_MOONS), 10))==179
print(f"Part 1: {energy(n_steps(clone_moons(moon_dat), 1000))}")

LCM = lambda a,b: a*b//gcd(a,b)

def period(moons):
    visited = [set(), set(), set()]
    cycle = [0, 0, 0]
    update_cycle = lambda c,v,s,it: c if c>0 else (it if s in v else 0)

    for i in count():
        x, y, z, dx, dy, dz = list(zip(*moons))
        state = [(x,dx), (y,dy), (z,dz)]
        cycle = [update_cycle(c, v, s, i) for c, v, s in zip(cycle, visited, state)]
        for v,s in zip(visited, state):
            v.add(s)
        if all(cycle):
            return LCM(cycle[0], LCM(cycle[1], cycle[2]))
        step(moons)

print(f"Part 2: {period(clone_moons(moon_dat))}")