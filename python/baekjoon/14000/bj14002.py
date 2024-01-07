n = int(input())
lst = [*map(int, input().split())]

g = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j] and g[i] < g[j] + 1:
            g[i] = g[j] + 1

print(max(g))

r = []
mxIdx = g.index(max(g))
r.append(lst[mxIdx])
l = max(g) - 1

for i in range(mxIdx - 1, -1, -1):
    if g[i] == l and lst[i] < r[-1]:
        r.append(lst[i])
        l -= 1

for i in [*reversed(r)]:
    print(end=f'{i} ')