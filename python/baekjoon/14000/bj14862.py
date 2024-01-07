import sys
sys.setrecursionlimit(10**6 + 1)

n = int(input())

d = [[0 for _ in range(2)] for _ in range(1_000_001)]
d[0][0] = 0
d[1][0] = 2
d[2][0] = 7
d[2][1] = 1

def dp(x):
    for i in range(3, x + 1):
        d[i][1] = (d[i - 1][1] + d[i - 3][0]) % 1_000_000_007
        d[i][0] = (3 * d[i - 2][0] + 2 * d[i - 1][0] + 2 * d[i][1]) % 1_000_000_007
    return d[x][0]


print(dp(n))