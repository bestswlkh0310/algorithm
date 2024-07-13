e1, s1, e2, s2 = map(int, input().split())

T = [
    (s1, e1),
    (s1, e2),
    (s2, e1),
    (s2, e2)
]

def func(x, y):
    n = max(abs(x), abs(y))
    s = 2 + n * (n - 1) // 2 * 8
    if x == n and y < n: # 1 area
        s += n - y - 1
    elif y == -n and x < n: # 2 area
        s += 2 * n - x + n - 1
    elif x == -n and y > -n: # 3 area
        s += 4 * n + y + n - 1
    elif y == n and x > -n: # 4 area
        s += 6 * n + x + n - 1
    else: # center
        s = 1
    return s

mxLen = len(str(max([func(x, y) for x, y in T])))

for y in range(e1, e2 + 1):
    for x in range(s1, s2 + 1):
        s = func(x, y)
        print(str(s).rjust(mxLen, ' '), end=' ')
    print()