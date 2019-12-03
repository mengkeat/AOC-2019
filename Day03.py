import os

with open("Day03.txt") as infile:
    l1_dat = infile.readline().strip().split(",")
    l2_dat = infile.readline().strip().split(",")

def trace(line):
    c = (0,0)
    for move in line:
        dist = int(move[1:])
        if move[0]=='R':
            c = (c[0]+dist, c[1])
        elif move[0]=='L':
            c = (c[0]-dist, c[1])
        elif move[0]=='U':
            c = (c[0], c[1]+dist)
        elif move[0]=='D':
            c = (c[0], c[1]-dist)
        yield move[0], dist, c
    

def get_horiz_vert_lines(d):
    vert, horiz = [], []
    vdist, hdist = [], []
    currpt = (0,0)
    acc_dist = 0
    for dir, dist, nextpt in trace(d):
        if dir=='R' or dir=='L':
            horiz.append([currpt, nextpt])
            hdist.append(acc_dist)
        elif dir=='U' or dir=='D':
            vert.append([currpt, nextpt])
            vdist.append(acc_dist)
        currpt = nextpt
        acc_dist += dist
    return vert, horiz, vdist, hdist

def intersect_points(vert, horiz, vdist, hdist):
    p, d = [], []
    for v, vd in zip(vert, vdist):
        x = v[0][0]
        y1, y2 = v[0][1], v[1][1]
        for h, hd in zip(horiz, hdist):
            x1, x2 = h[0][0], h[1][0]
            y = h[0][1]
            if x>=min(x1,x2) and x<=max(x1,x2) and y>=min(y1,y2) and y<=max(y1,y2) and x!=0 and y!=0:
                p.append((x,y))
                d.append(abs(x-x1)+abs(y-y1)+vd+hd)
    return p, d

def nearest(line1, line2):
    v1, h1, vd1, hd1 = get_horiz_vert_lines(line1)
    v2, h2, vd2, hd2 = get_horiz_vert_lines(line2)

    pts1, line_dist1 = intersect_points(v1, h2, vd1, hd2)
    pts2, line_dist2 = intersect_points(v2, h1, vd2, hd1)

    dist_l1 = lambda x: abs(x[0])+abs(x[1])
    l1_dist1 = [dist_l1(x) for x in pts1]
    l1_dist2 = [dist_l1(x) for x in pts2]

    min_l1_dist = min(l1_dist1+l1_dist2)
    min_line_dist = min(line_dist1+line_dist2)

    return min_l1_dist, min_line_dist

# Assume no overlapping lines
print(nearest( ["R8", "U5", "L5", "D3"], ["U7", "R6", "D4", "L4"]))

assert nearest( ["R75","D30","R83","U83","L12","D49","R71","U7","L72"], ["U62","R66","U55","R34","D71","R55","D58","R83"] ) == (159, 610)
assert nearest( ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"], ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"] ) == (135, 410)

print(nearest(l1_dat, l2_dat))

