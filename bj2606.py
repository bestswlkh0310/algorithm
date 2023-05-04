n = int(input())
k = int(input())

node = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
for i in range(k):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

cnt = 0
q = [node[1]]
while len(q) != 0:
    linked = q[0]
    del q[0]
    for i in linked:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            q.append(node[i])
print(cnt - 1)