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

N, REP = 119315717514047, 101741582076661
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

def modinv(a, m):
    g, x, y = egcd(a, m) 
    return (None if g!=1 else x%m)

# Trace forward first to obtain new sequence p0 + (p1-p0) * x (as all sequences can be)
# represented as a*x+b 
# Then mathematically compute the inverse. We know that to map back to factory order,
# f(a*x+b)=x where f(i) is the inverse transformation to be obtained i.e. f(i) = a_t*i + b_t 
# when x=0, a_t*b + b_t = 0    ------------- (1)
# when x=1, a_t*a + a_t*b + b_t = 1 ------------- (2)
# Take (2)-(1): a_t*a=1 ---> a_t = modinv(a, N)
# then substitue a_t back to (1) ----> b_t = -a_t*b (congruent mod N)
# Then apply the polynomial expansion of f^repetitions to obtain final reverse position
p0, p1 = track_pos(0), track_pos(1)
a1, b1 = (p1-p0)%N, p0
a_t = modinv(a1, N) 
b_t = (-a_t*b1)%N

poly = lambda x: pow(a_t, REP, N)*x + (pow(a_t, REP, N)-1) * modinv(a_t-1, N) * b_t
print(f"Part 2: {poly(2020)%N}")