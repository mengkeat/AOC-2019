from collections import Counter
from itertools import dropwhile

with open("Day08.txt") as infile:
    dat = infile.readline().strip()
    l = 25*6
    layers = [dat[i:i+l] for i in range(0, len(dat), l)]
    print(len(layers))

layer_counts = list(map(Counter, layers))
fewest_zero = min(layer_counts, key = lambda x: x['0'])

print(f"Part 1: {fewest_zero['1']*fewest_zero['2']}")

visible_pixel = lambda l: next(dropwhile(lambda x: x=='2', l))
visible_image = "".join([visible_pixel(p) for p in zip(*layers)])
visible_image = visible_image.replace("0", " ")

for i in range(0, len(visible_image), 25):
    print(visible_image[i:i+25])