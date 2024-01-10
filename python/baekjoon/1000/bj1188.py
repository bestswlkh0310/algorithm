import math

a, b = map(int, input().split())
print(b - math.gcd(a, b))