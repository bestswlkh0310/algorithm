from collections import deque

n, m = map(int, input().split())
A = [[] for _ in range(n)] # idx: 노드, i: 그 노드의 인접노드
v = [0 for _ in range(n)] # 진입차수

def topology_sort():

    q = deque()

    for (idx, i) in enumerate(v):
        if i == 0:
            q.append(idx)

    result = []

    for i in range(n):
        x = q.popleft()
        result.append(x)
        for j in A[x]:
            v[j] -= 1
            if v[j] == 0:
                q.append(j)
    
    for i in [i + 1 for i in result]:
        print(end=f'{i} ')


if __name__ == '__main__':
    for _ in range(m):
        a, b = map(int, input().split())
        A[a - 1].append(b - 1)
        v[b - 1] += 1
    topology_sort()