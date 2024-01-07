from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(x):
    global id
    id += 1
    d[x] = id
    s.append(x)

    parent = id

    for i in A[x]:
        if d[i] == 0:
            parent = min(parent, dfs(i))
        elif not v[i]:
            parent = min(parent, d[i])
    
    if d[x] == parent:
        scc = []
        while True:
            t = s.pop()
            scc.append(t)
            v[t] = True
            if t == x:
                break
        SCC.append(scc)

    return parent

n, e = map(int, input().split())

A = [[] for _ in range(n)]
d = [0 for _ in range(n)]
v = [False for _ in range(n)]
SCC = []
s = []
id = 0

for i in range(e):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A[a].append(b)

for i in range(n):
    if d[i] == 0:
        dfs(i)

A1 = A[:]
v = [0 for _ in range(len(SCC))] # 진입차수
A = [-1 for _ in range(n)]

for i in range(len(SCC)):
    for j in SCC[i]:
        A[j] = i
# print(SCC)

result = [False for _ in range(len(SCC))]
# cnt = 0
for (idx, i) in enumerate(SCC): # idx -> j
    for j in i:
        for k in A1[j]:
            # cnt += 1
            if idx != A[k]:
                result[A[k]] = True
# print(result)
print(result.count(False))