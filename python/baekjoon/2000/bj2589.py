import sys
from collections import deque

input = sys.stdin.readline
h, w = map(int, input().split())
G = [list(input()) for _ in range(h)]
R = [[0 for _ in range(w)] for _ in range(h)]

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

for i in range(h):
    for j in range(w):
        if G[i][j] == "W":
            continue
        q = deque([(i, j, 1)])
        v = [[0 for _ in range(w)] for _ in range(h)]
        v[i][j] = 1
        while q:
            y, x, cnt = q.popleft()
            for xy in dxy:
                y1, x1 = xy
                y1 += y
                x1 += x
                if 0 <= y1 < h and 0 <= x1 < w and G[y1][x1] == "L" and not v[y1][x1]:
                    q.append((y1, x1, cnt + 1))
                    v[y1][x1] = cnt + 1
        for k in range(h):
            for l in range(w):
                R[k][l] = max(R[k][l], v[k][l])

        # for k in v:
        #     print(k)
        # print()

print(max([max(i) for i in R]) - 1)
