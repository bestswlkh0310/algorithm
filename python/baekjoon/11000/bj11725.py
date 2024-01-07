from collections import deque
import sys
I=sys.stdin.readline
n=int(I())
A=[[] for _ in range(n)]
V=[False for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    A[a - 1].append(b - 1)
    A[b - 1].append(a - 1)

q = deque([0])

R=[-1 for _ in range(n)]

while q:
    x = q.popleft()
    for i in A[x]:
        if not V[i]:
            V[i] = True
            R[i] = x
            q.append(i)
del R[0]
for i in R:
    print(i + 1)