import collections
import sys

n, m, start = map(int, sys.stdin.readline().split())
arr = [[] for i in range(n + 1)]
visit = [-1 for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(n + 1):
    arr[i].sort()
q = collections.deque()
q.append((start, 1))
visit[start] = 0
cnt = 1
while q:
    (x, n1) = q.popleft()
    for i in arr[x]:
        if visit[i] == -1:
            cnt += 1
            visit[i] = n1 * cnt
            q.append((i, n1 + 1))
del visit[0]
print(sum([i for i in visit if i != -1]))
