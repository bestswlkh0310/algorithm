import sys
import collections
n, m, start = map(int, sys.stdin.readline().split())
arr = [[] for i in range(n + 1)]
visit = [0 for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
visit[start] = 1
for i in range(1, n + 1):
    arr[i].sort(reverse=True)

cnt = 1
stack = collections.deque()
stack.extend(arr[start])
while stack:
    x = stack.pop()
    if visit[x] == 0:
        stack.extend(arr[x])
        cnt += 1
        visit[x] = cnt
del visit[0]
for i in visit:
    sys.stdout.write(f"{i}\n")