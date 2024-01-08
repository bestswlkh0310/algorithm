n, m = map(int, input().split())

inf = int(1e9)

edges = []
d = [inf for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((a - 1, b - 1, w))

def df(x):
    d[x] = 0
    for i in range(n):
        for j in range(m):
            s, e, w = edges[j]
            if d[s] != inf and d[e] > d[s] + w:
                d[e] = d[s] + w
                if i == n - 1:
                    return True

    return False

if df(0):
    print(-1)
else:
    for i in d[1:]:
        if i != inf:
            print(i)
        else:
            print(-1)
