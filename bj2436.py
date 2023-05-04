import sys
def gcd(a, b):
    if b != 0:
        return gcd(b, a % b)
    else:
        return a

a, b = map(int, sys.stdin.readline().split())
q = 0
w = 99999999999999
r1 = 0
r2 = 0
for i in range(1, 10000):
    c = a * i
    e = b // c * a
    # print(c, e)
    if (b / c) % 1 == 0.0 and (b / e) % 1 == 0.0:
        if w > c + e and a * b // gcd(c, e) == b:
            w = c + e
            r1 = c
            r2 = e
print(r1, r2)