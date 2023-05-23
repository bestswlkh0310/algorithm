import collections
a, b, c = map(int, input().split())
q = collections.deque()
q.append((0, 0, c))

arr = []

while q:
    (a1, b1, c1) = q.popleft()
    if a1 == 0:
        arr.append(c1)
    q.append((a1 + c1, b1, 0))
    q.append((a1, b1 + c1, 0))
    q.append(())