from collections import deque
import sys

input = sys.stdin.readline


# 2 ≤ N ≤ 1000
# 1 ≤ K ≤ 100,000
# 1 ≤ X, Y, W ≤ N


for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = [*map(int, input().split())]
    v = [0 for _ in range(n)]

    dArr = []
    visit = [False for _ in range(k)]

    for _ in range(k):
        y, x = map(int, input().split())
        dArr.append((x - 1, y - 1))

    w = int(input()) - 1
    
    v[w] = lst[w]

    q = deque()
    q.append(w)

    while q:
        s = q.popleft()
        for (idx, i) in enumerate(dArr):
            start = i[0]
            end = i[1]
            if start == s:
                if not visit[idx] and v[end] < v[start] + lst[end]:
                    visit[idx] = True
                    v[end] = v[start] + lst[end]
                    q.append(end)
                elif visit[idx]:
                    v[start] -= lst[start]

    # print(v)
    print(max(v))

# 1
# 3 3
# 1 2 3
# 1 2
# 2 3
# 3 1
# 1