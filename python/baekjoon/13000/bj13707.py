n, k = map(int, input().split()) # 6 4

if k == 1:
    print(1)
    exit(0)

d = [[None for _ in range(n + 1)] for _ in range(k - 1)]

w = 1_000_000_000

for i in range(k - 1):
    for j in range(n + 1):
        if j == 0:
            d[i][j] = 1
        elif i == 0:
            d[i][j] = 1 + d[i][j - 1] % w
        else:
            d[i][j] = d[i - 1][j] + d[i][j - 1] % w

print(d[-1][-1] % w)