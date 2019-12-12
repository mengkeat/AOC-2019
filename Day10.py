from math import gcd, atan2, pi
from itertools import zip_longest, groupby

with open("Day10.txt") as infile:
    dat = [x.strip() for x in infile.readlines()]
    asteroids = [(c, r) for r, row in enumerate(dat) for c, col in enumerate(row) if col=="#"]

diff = lambda x, y: (y[0]-x[0], y[1]-x[1])

def basic(vec):
    s = gcd(vec[0], vec[1])
    return vec if s==0 else (vec[0]//s, vec[1]//s)

diff_vec = lambda ref_pt: [diff(ref_pt, p) for p in asteroids]
basic_vec = lambda vec: [basic(p) for p in vec]

best_x, best_y, best_loc_count = max([(*x, len(set(basic_vec(diff_vec(x))))) for x in asteroids], key=lambda x:x[2])
print(f"Part 1: {best_loc_count-1} at {best_x}, {best_y}")

def compute_angle(c,r):
    a = atan2(r, c)
    a = a+2.0*pi if a<0 else a
    a += pi/2.0
    a = a-2.0*pi if a>2.0*pi else a
    return a

best_diff_vec = diff_vec((best_x, best_y))
all_angles = [compute_angle(*v) for v in best_diff_vec]
all_dist = [c*c+r*r for (c,r) in best_diff_vec]
sorted_pts = sorted(filter(lambda x: x[1]!=0, zip(all_angles, all_dist, asteroids)))

l = zip_longest(*[list(g) for _,g in groupby(sorted_pts, key=lambda x:x[0])])
expanded = [x for g in l for x in g if x != None]
print(expanded[199])
# all_angles = lambda ref_pt: [atan2(c,r)-pi/2.0 for (c,r) in [diff(ref_pt, p) for p in asteroids]]
# sorted_pts = sorted(zip(all_angles((best_x, best_y)), get_basic_vec, asteroids))