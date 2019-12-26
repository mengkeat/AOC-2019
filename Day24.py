from collections import defaultdict

eris = [x.strip() for x in open("Day24.txt").readlines()]
D = [(-1,0), (1,0), (0,-1), (0, 1)]

def rating(m): return int("".join(m)[::-1].replace('#', '1').replace('.','0'), 2)
def map_at(m, l, r, c): return m[l][r][c]=='#'
def new_dict(): return defaultdict(lambda: ['.'*5 for _ in range(5)])
def showmap(m): print("\n".join(m))

def neigh_coords(m, l, r, c):
    neighs = [(l, r+dr, c+dc) for dr, dc in D]
    new = set()
    for l1, r1, c1 in neighs:
        if   r1<0: new.add((l-1, 1, 2))
        elif r1>4: new.add((l-1, 3, 2))
        elif c1<0: new.add((l-1, 2, 1))
        elif c1>4: new.add((l-1, 2, 3))
        elif (r1,c1)==(2,2):
            if   (r,c)==(2,1): new |= set([(l+1, i, 0) for i in range(5)])
            elif (r,c)==(2,3): new |= set([(l+1, i, 4) for i in range(5)])
            elif (r,c)==(1,2): new |= set([(l+1, 0, i) for i in range(5)])
            elif (r,c)==(3,2): new |= set([(l+1, 4, i) for i in range(5)])
        else:
            new.add((l1, r1, c1))
    return new

def neigh_count(m, l, r, c, recurse=False): 
    if recurse:
        return sum([map_at(m, l1, r1, c1) for l1, r1, c1 in neigh_coords(m,l,r,c)])
    else:
        coords = [(r+dr, c+dc) for dr, dc in D]
        return sum([map_at(m, l, nr, nc) for nr, nc in coords if 0<=nr<5 and 0<=nc<5])

def evolve(m, recurse=False):
    new_m = new_dict()
    curr_keys = list(m.keys())
    for l in curr_keys:
        new_lvl  = []
        for r in range(5):
            s = ""
            for c in range(5):
                nc = neigh_count(m, l, r, c, recurse)
                if (r,c)==(2,2) and recurse:
                    s += "."
                elif map_at(m, l, r,c):
                    s += "#" if nc==1 else "."
                elif not map_at(m, l, r,c):
                    s += "#" if (nc==1 or nc==2) else "."
            new_lvl.append(s)
        new_m[l] = new_lvl
    if recurse:
        min_k, max_k = min(curr_keys), max(curr_keys)
        if rating(new_m[min_k])>0: new_m[min_k-1]
        if rating(new_m[max_k])>0: new_m[max_k+1]
    return new_m

lvl_map = new_dict()
lvl_map[0] = list(eris)

# For part 1
seen = set([rating(lvl_map[0])])
while True:
    lvl_map = evolve(lvl_map)
    if rating(lvl_map[0]) in seen:
        showmap(lvl_map[0])
        print(f"Part 1: {rating(lvl_map[0])}")
        break
    else:
        seen.add(rating(lvl_map[0]))

lvl_map2 = new_dict()
lvl_map2[0] = list(eris)
lvl_map2[-1], lvl_map2[1]

for _ in range(200):
    lvl_map2 = evolve(lvl_map2, True)

# a, b = min(lvl_map2.keys()), max(lvl_map2.keys())
# for d in range(a,b):
#     print("Depth: ", d)
#     showmap(lvl_map2[d])

def count_map(m): return sum([x.count("#") for x in m])
p2 = sum([count_map(m) for m in lvl_map2.values()])
print(f"Part 2: {p2}")
