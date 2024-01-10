import collections

n, k = map(int, input().split())
v = [1_000_000 for _ in range(100_001)]
q = collections.deque()

q.append((n, 0))
result = None
while q:
    (x1, n1) = q.popleft()
    if x1 == k:
        result = n1
        break
    if 0 <= x1 - 1 <= 100_000 and n1 + 1 < v[x1 - 1]:
        v[x1 - 1] = n1 + 1
        q.append((x1 - 1, n1 + 1))
    if 0 <= x1 + 1 <= 100_000 and n1 + 1 < v[x1 + 1]:
        v[x1 + 1] = n1 + 1
        q.append((x1 + 1, n1 + 1))
    if 0 <= x1 * 2 <= 100_000 and x1 != 0 and n1 < v[x1 * 2]:
        v[x1 * 2] = n1
        q.append((x1 * 2, n1))

print(result)
