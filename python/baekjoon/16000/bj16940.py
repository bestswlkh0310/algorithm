import sys
from collections import deque

input=sys.stdin.readline

n = int(input())

g = [[] for _ in range(n)]
v = [False for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)

q = deque([0])
v[0] = True
r = [i - 1 for i in [*map(int, input().split())]]

if r[0] != 0:
    print(0)
    exit(0)
del r[0]

while q:
    x = q.popleft()
    cnt = 0
    for i in g[x]:
        if not v[i]:
            cnt += 1
    for _ in range(cnt):
        if r[0] in g[x] and v[r[0]] == False:
            q.append(r[0])
            v[r[0]] = True
            del r[0]
        else:
            print(0)
            exit(0)

if len(r):
    print(0)
else:
    print(1)

# 5
# 1 2
# 2 5
# 1 3
# 3 4
# 1 2 3 4 5

# 1 2 3 5 4, 혹은 1 3 2 4 5