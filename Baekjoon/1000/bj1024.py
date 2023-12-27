import math

n, k = map(int, input().split())

for i in range(max(2, k), n + 2):
    if i > 100:
        break
    if (n / float(i) % 1) == 0.5 or (i % 2 == 1 and n / float(i) % 1 == 0.0):
        if int(math.ceil(n / i)) - i // 2 < 0:
            continue
        for j in range(i):
            print(int(math.ceil(n / i)) - i // 2 + j)

        exit(0)
print(-1)