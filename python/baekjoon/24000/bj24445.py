import collections
import sys
n, m, start = map(int, sys.stdin.readline().split())
arr = [[] for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
q = collections.deque()
q.append(start)
visit[start] = 1

for i in range(1, n + 1):
    arr[i].sort(reverse=True)
cnt = 1
while q:
    x = q.popleft()
    for i in arr[x]:
        if visit[i] == 0:
            cnt += 1
            visit[i] = cnt
            q.append(i)
for i in range(1, n + 1):
    sys.stdout.write(f"{visit[i]}\n")