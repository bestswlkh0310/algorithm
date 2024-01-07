# 2644 - 촌수계산
import collections

n = int(input())
a, b = map(int, input().split())
k = int(input())
lst = [[] for i in range(n + 1)]
visit = [False] * (n + 1)

for i in range(k):
    c, v = map(int, input().split())
    lst[c].append(v)
    lst[v].append(c)
q = collections.deque()
mx = 0
q.append((a, 0))
mn = 99999
while q:
    if mx < len(q): mx = len(q)
    (m, n1) = q.popleft()
    visit[m] = True
    if m == b:
        mn = n1
        continue
    if n1 >= n:
        continue
    for i in lst[m]:
        if not visit[i]:
            q.append((i, n1 + 1))

if mn == 99999: print(-1)
else: print(mn)
