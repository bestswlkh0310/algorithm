# 1: 9 * 1 (1~9)
# 2: 90 * 2 (10~99)
# 3: 900 * 3 (100~999)

n = int(input())

i = 0
s = 0
while n - (9 * (10 ** i)) > 0:
    n -= (9 * (10 ** i))
    s += (9 * (10 ** i)) * (i + 1)
    i += 1
print(s + n * (i + 1))