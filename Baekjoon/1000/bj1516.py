from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
lst = [0 for _ in range(n)]
v = [-1 for _ in range(n)]

dArr = [[] for _ in range(n)]

for i in range(n):
    l = [*map(int, input().split())]
    lst[i] = l[0]
    if len(l) > 2:
        for j in range(1, len(l) - 1):
            dArr[l[j] - 1].append(i)

for i in range(n):
    if v[i] == -1:
        v[i] = lst[i]

    q = deque([i])

    while q:
        s = q.popleft()
        for (idx, i) in enumerate(dArr[s]):
            start = s
            end = i
            if v[end] < v[start] + lst[end]:
                v[end] = v[start] + lst[end]
                q.append(end)

for i in v:
    print(i)