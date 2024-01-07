n = int(input())

arr = [False for _ in range(1001)]

def dp(x):
    if x == 1: return 1
    if x == 2: return 3
    if arr[x]: return arr[x]
    arr[x] = (dp(x - 1) + 2 * dp(x - 2)) % 10007
    return arr[x]

print(dp(n))