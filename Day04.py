from itertools import groupby
low, high = 278384, 824795

increasing = lambda s: sorted(s)==list(s)
grp_len = lambda s: [len(list(g)) for _, g in groupby(s)]
adjacent_same = lambda s: any(map(lambda x: x>=2, grp_len(s)))
valid = lambda s: increasing(s) and adjacent_same(s)

# Part 1
print(sum( map(lambda x: valid(str(x)), range(low, high+1))))

# Part 2
adjacent_same2 =  lambda s: any(map(lambda x: x==2, grp_len(s)))
valid2 = lambda s: increasing(s) and adjacent_same2(s)

print(sum( map(lambda x: valid2(str(x)), range(low, high+1))))
