import sys
import collections
n, m, start = map(int, sys.stdin.readline().split())
arr = [[] for i in range(n + 1)]
visit = [-1 for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
visit[start] = 1
for i in range(1, n + 1):
    arr[i].sort()
cnt = 1
stack = collections.deque()
visit[start] = 0
result = 0
for i in arr[start]:
    stack.append((i, 1))
while stack:
    (x, n1) = stack.pop()
    if visit[x] == -1:
        cnt += 1
        result += n1 * cnt
        for i in arr[x]:
            stack.append((i, n1 + 1))
        visit[x] = n1
del visit[0]

print(result)
