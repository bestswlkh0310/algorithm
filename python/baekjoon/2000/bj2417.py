import math
inp = int(input())
v = math.isqrt(inp)
if inp != v ** 2:
    v += 1

print(v)