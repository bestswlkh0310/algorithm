import math

d = 1_000_000_007

a, x = map(int, input().split())

n = math.floor(math.log(x, 2))

arr = [(a, 1)]

for i in range(1, n + 1):
    arr.append(((arr[i - 1][0] ** 2) % d, i + 1))

s = 1

bArr = list(map(int, reversed(list(str(bin(x))[2:]))))

for (idx, i) in enumerate(bArr):
    if i == 1:
        s = (s * (arr[idx][0]) % d) % d

print(s)