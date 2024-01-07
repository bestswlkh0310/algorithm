import sys
import collections

dx = ((1, 0), (-1, 0), (0, 1), (0, -1))
arr = []
n = int(input())
mx = 0
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    x = max(a)
    mx = x if x > mx else mx
    arr.append(a)
mmm = 0


for h in range(0, mx + 1):
    world = []
    q = collections.deque()
    # True화
    for i in arr:
        b = []
        for j in i:
            b.append(h >= j)
        world.append(b)
    s = 0
    for (y, i) in enumerate(world):
        for (x, j) in enumerate(i):
            if not j:
                s += 1
                q.append((y, x))
                world[y][x] = True
                while q:
                    (y1, x1) = q.popleft()
                    for k in dx:
                        mx = x1 + k[0]
                        my = y1 + k[1]
                        if 0 <= mx < n and 0 <= my < n and not world[my][mx]:
                            world[my][mx] = True
                            q.append((my, mx))
    if s > mmm:
        mmm = s
    # True = 물에 잠김

print(mmm)