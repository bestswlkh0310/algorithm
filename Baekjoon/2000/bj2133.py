n = int(input())

arr = [False for _ in range(31)]

def dp(x):
    if x == 0: return 1
    if x == 1: return 0
    if x == 2: return 3
    if arr[x] != False: return arr[x]
    s = 3 * dp(x - 2)
    for i in range(4, x + 1, 2):
        s += 2 * dp(x - i)

    arr[x] = s
    return arr[x]

print(dp(n))