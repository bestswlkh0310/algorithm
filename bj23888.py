import math
import sys

a, d = map(int, sys.stdin.readline().split())
for _ in range(int(sys.stdin.readline())):
    m, s, e = map(int, sys.stdin.readline().split())
    v = (e - s + 1) * (a + (s - 1) * d + a + (e - 1) * d) // 2
    if m == 1:
        print(v)
    else:
        result = a + (s - 1) * d
        for i in range(a + s * d, a + (e - 1) * d + 1, d):
            result = math.gcd(result, i)
        print(result)
