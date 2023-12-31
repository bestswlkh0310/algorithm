from collections import deque

n, m = map(int, input().split())

g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    g[a - 1].append((b - 1, w))
    g[b - 1].append((a - 1, w))

for _ in range(m):
    a, b = map(int, input().split())
    q = deque([(a - 1, 0)])
    v = [False for _ in range(n)]
    v[a - 1] = True
    t = True
    while q and t:
        (x, w) = q.popleft()
        for (d, w1) in g[x]:
            if not v[d]:
                if d == b - 1:
                    print(w + w1)
                    t = False
                    break
                v[d] = True
                q.append((d, w + w1))
