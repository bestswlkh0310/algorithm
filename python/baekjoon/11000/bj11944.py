import math
n, m = input().split()
if len(n) * int(n) < int(m):
    print(n * int(n))
else:
    print(str(n * math.ceil(int(m) / len(n)))[:int(m)])