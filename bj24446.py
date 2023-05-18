import collections
import sys

n, m, start = map(int, sys.stdin.readline().split())
arr = [[] for i in range(n + 1)]
visit = [-1 for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
q = collections.deque()
q.append((start, 1))
visit[start] = 0
while q:
    (x, n) = q.popleft()
    for i in arr[x]:
        if visit[i] == -1:
            visit[i] = (n)
            q.append((i, n + 1))
del visit[0]
for i in visit:
    sys.stdout.write(f"{i}\n")
sys.stdout.flush()
sys.stdout.close()
