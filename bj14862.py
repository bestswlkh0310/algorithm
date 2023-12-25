import sys
sys.setrecursionlimit(10**6 + 1)

n = int(input())

arr = [False for _ in range(1_000_001)]

def dp(x):
    if x == 0: return 1
    if x == 1: return 2
    if x == 2: return 7
    if arr[x] != False: return arr[x]
    s = 3 * dp(x - 2) + 2 * dp(x - 1)
    for i in range(3, x + 1):
        s += (2 * dp(x - i)) % 100_000_007
    arr[x] = s
    return arr[x] % 100_000_7

print(dp(n))