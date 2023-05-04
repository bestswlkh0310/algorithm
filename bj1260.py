n, m, v = map(int, input().split())
dfsVisited = [False] * (n + 1)
bfsVisited = [False] * (n + 1)
dfsNode = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    dfsNode[a].append(b)
    dfsNode[b].append(a)
for i in range(1, n + 1):
    dfsNode[i] = sorted(dfsNode[i])
bfsNode = dfsNode.copy()


def dfs(v):
    for i in dfsNode[v]:
        if not dfsVisited[i]:
            dfsVisited[i] = True
            print(i, end=" ")
            dfs(i)


dfsVisited[v] = True
print(v, end=" ")
dfs(v)
print()
bfsVisited[v] = True
print(v, end=" ")

q = [bfsNode[v]]
while len(q) != 0:
    v = q[0]
    del q[0]
    for i in v:
        if not bfsVisited[i]:
            bfsVisited[i] = True
            print(i, end=" ")
            q.append(bfsNode[i])
