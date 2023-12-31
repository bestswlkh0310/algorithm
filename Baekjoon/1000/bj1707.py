from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    v, e = map(int, input().split())
    g = [[] for _ in range(v)]
    visit = [-1 for _ in range(v)]

    for _ in range(e):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    # print(g)
    t = True
    for i in range(v):
        q = deque([(i, False)])
        if visit[i] != -1:
            continue
        visit[i] = False
        while q and t:
            # print(i, q, visit)
            (x, d) = q.popleft()
            for j in g[x]:
                if visit[j] == -1:
                    q.append((j, not d))
                    visit[j] = not d
                elif visit[j] == d:
                    t = False
                    # print(x, j, visit)
                    break
    print('YES' if t else 'NO')