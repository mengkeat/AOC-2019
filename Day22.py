from itertools import *
from math import gcd

shuffles = [x.strip().split() for x in open("Day22.txt").readlines()]
N = 10007
new_stack_i = lambda i: N-i-1
cut_i = lambda i, n:  (i-n)%N
deal_i = lambda i, n: (i*n)%N

def track_pos(i):
    for shuf in shuffles:
        if shuf[0]=="cut":
            i = cut_i(i, int(shuf[1]))
        elif shuf[0]=="deal" and shuf[2]=="increment":
            i = deal_i(i, int(shuf[-1]))
        elif shuf[0]=="deal" and shuf[-1]=="stack":
            i = new_stack_i(i)
    return i
print(f"Part 1: {track_pos(2019)}")

N, REPEAT = 119315717514047, 101741582076661
# def egcd(a, b):
#     x,y, u,v = 0,1, 1,0
#     while a != 0:
#         q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
#         b,a, x,y, u,v = a,r, u,v, m,n
#     return b, x, y

# def modinv(a, m):
#     g, x, y = egcd(a, m) 
#     if g != 1:
#         return None
#     else:
#         return x % m
# LCM = lambda a,b: a*b//gcd(a,b)

# print(log(REPEAT))

# a, b, L = 7, 4, 10
# A = [9,2,5,8,1,4,7,0,3,6]
# lst = list(range(10))
# for _ in range(10):
#     for i in A:
#     print(lst)