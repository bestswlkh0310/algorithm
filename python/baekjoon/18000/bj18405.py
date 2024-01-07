import sys
from collections import deque
input=sys.stdin.readline
I=lambda:[*map(int, input().split())]
n, k = I()
g = [I() for _ in range(n)]
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
s, x2, y2 = I()
for _ in range(s):
    vi = [False for _ in range(k)]
    for i in range(n):
        for j in range(n):
            q = deque([(i, j, 0)])
            if vi[g[i][j] - 1]:
                continue
            while q:
                (y, x, cnt) = q.popleft()
                for (dy, dx) in dxy:
                    x1 = x + dx
                    y1 = y + dy
                    if 0 <= x1 < n and 0 <= y1 < n and cnt == 0 and g[y1][x1]:
                        g[y1][x1] = g[y][x]
                        vi[g[y][x] - 1] = True
                        q.append((y1, x1, cnt + 1))

print(g[x2 - 1][y2 - 1])