V, E = map(int, input().split())
K = int(input())

INF = 11

# 그래프
arr = [[0 if i == j else INF for i in range(V)] for j in range(V)]

# 방문 여부
visit = [False for _ in range(V)]
d = [INF for _ in range(V)]

# 입력받기
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u - 1][v - 1] = w

def smallIdx():
    min = INF
    idx = 0
    for i in range(V):
        # 최소값보다 작고 방문하지 X
        if d[i] < min and not visit[i]:
            min = d[i]
            idx = i

    return idx

# dijkstra
def dijkstra(start):
    for i in range(V):
        d[i] = arr[start][i]

    visit[start] = True
    for i in range(V - 2):
        current = smallIdx()
        visit[current] = True
        for j in range(V):
            if not visit[j] and d[current] + arr[current][j] < d[j]:
                d[j] = d[current] + arr[current][j]

dijkstra(K - 1)
for i in d:
    if i != INF:
        print(i)
    else:
        print('INF')