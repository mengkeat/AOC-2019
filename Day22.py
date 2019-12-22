from itertools import *

shuffles = [x.strip().split() for x in open("Day22.txt").readlines()]
cards = list(range(10007))
# cards = list(range(10))

deal_new_stack = lambda x: x[::-1]
cut_n = lambda x, n: x[n:]+x[:n]
def deal_incr(x, n): 
    L = len(x)
    x1 = [0]*L
    for i in range(len(x)):
       x1[ (i*n)%L ] = x[i]
    return x1

for shuf in shuffles:
    if shuf[0]=="cut":
        cards = cut_n(cards, int(shuf[1]))
    elif shuf[0]=="deal" and shuf[2]=="increment":
        cards = deal_incr(cards, int(shuf[-1]))
    elif shuf[0]=="deal" and shuf[-1]=="stack":
        cards = deal_new_stack(cards)

# print(cards)
print(f"Part 1: {cards.index(2019)}")

# L2, REPEAT = 119315717514047, 101741582076661