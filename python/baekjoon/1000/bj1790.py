# 1: 9 * 1 (1~9)
# 2: 90 * 2 (10~99)
# 3: 900 * 3 (100~999)

# 23 - 9 = 14
# 14 // 2 = 7

import math

n, k = map(int, input().split())

k1 = k
i = 0
while k1 - (9 * (10 ** i)) * (i + 1) > 0:
    k1 -= (9 * (10 ** i)) * (i + 1)
    i += 1


n1 = n
j = 0
s = 0
while n1 - (9 * (10 ** j)) > 0:
    n1 -= (9 * (10 ** j))
    s += (9 * (10 ** j)) * (j + 1)
    j += 1
len = s + n1 * (j + 1)

n1 = i + 1 # 자리수
v = math.ceil((int('9' * i) if i != 0 else 0) + k1 / n1)
m = (k1 - 1) % (i + 1)
if len < k:
    print(-1)
else:
    print(str(v)[m])