import collections
import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[] for i in range(n + 1)]
visit = [False] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
cnt = 0
for i in range(1, n + 1):
    q = collections.deque()
    q.append(i)
    if not visit[i]:
        cnt += 1
        while q:
            x = q.popleft()
            for k in arr[x]:
                if not visit[k]:
                    visit[k] = True
                    q.append(k)
print(cnt)