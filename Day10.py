from math import gcd, atan2, pi
from itertools import zip_longest, groupby

with open("Day10.txt") as infile:
    dat = [x.strip() for x in infile.readlines()]
    asteroids = [(c, r) for r, row in enumerate(dat) for c, col in enumerate(row) if col=="#"]

diff = lambda x, y: (y[0]-x[0], y[1]-x[1])

def basic(x, y):
    s = gcd(x, y)
    return (x,y) if s==0 else (x//s, y//s)

diff_vec = lambda ref_pt: [diff(ref_pt, p) for p in asteroids]
basic_vec = lambda vec: [basic(*p) for p in vec]

best_x, best_y, best_loc_count = max([(*x, len(set(basic_vec(diff_vec(x))))) for x in asteroids], key=lambda x:x[2])
print(f"Part 1: {best_loc_count-1} at {best_x}, {best_y}")

compute_angle = lambda c,r: atan2(c, -r) % (2.0*pi)
best_diff_vec = diff_vec((best_x, best_y))
all_angles = [compute_angle(*v) for v in best_diff_vec]
all_dist = [c*c+r*r for (c,r) in best_diff_vec]
sorted_pts = sorted(filter(lambda x: x[1]!=0, zip(all_angles, all_dist, asteroids)))
l = zip_longest(*[list(g) for _,g in groupby(sorted_pts, key=lambda x:x[0])])
expanded = [x for g in l for x in g if x != None]
print(f"Part 2: {expanded[199]}")