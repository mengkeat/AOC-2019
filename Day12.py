import re
from itertools import permutations, repeat, starmap

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
assert energy(n_steps(TEST_MOONS, 10))==179
print(f"Part 1: {energy(n_steps(clone_moons(moon_dat), 1000))}")


