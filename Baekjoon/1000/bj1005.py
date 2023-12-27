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

    dArr = [[] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        dArr[y - 1].append(x - 1)

    w = int(input()) - 1
    
    v[w] = lst[w]

    q = deque([w])

    while q:
        s = q.popleft()
        for (idx, i) in enumerate(dArr[s]):
            start = s
            end = i
            # print('start -',start, end)
            # if start == s:
            if v[end] < v[start] + lst[end]:
                v[end] = v[start] + lst[end]
                q.append(end)

    # print(v)
    print(max(v))

# 1
# 3 3
# 1 2 3
# 1 2
# 2 3
# 3 1
# 1