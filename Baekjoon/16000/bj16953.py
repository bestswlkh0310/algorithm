import collections

q = collections.deque()

a, b = map(int, input().split())

mn = -1
q.append([a, 1])
while q:
    va = q.popleft()
    v = va[0]
    n = va[1]
    if v >= b:
        if v == b:
            if mn > v or mn == -1: mn = n
    else:
        q.append([v * 2, n + 1])
        q.append([int(str(v) + "1"), n + 1])
print(mn)