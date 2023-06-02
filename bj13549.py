import collections

n, k = map(int, input().split())

q = collections.deque()
q.append((n, 0))
result = None
while q:
    (x1, n1) = q.popleft()
    if x1 == k:
        result = n1
        break
    if 0 <= x1 - 1 <= 100_000:
        q.append((x1 - 1, n1 + 1))
    if 0 <= x1 + 1 <= 100_000:
        q.append((x1 + 1, n1 + 1))
    if 0 <= x1 * 2 <= 100_000 and x1 != 0:
        q.append((x1 * 2, n1))

print(result)
