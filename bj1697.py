import collections
import sys

a, b = map(int, input().split())
mn = sys.maxsize

q = collections.deque()
q.append((a + 1, 1))
q.append((a - 1, 1))
q.append((a * 2, 1))

while q:
    (s, n) = q.popleft()
    if n >= mn:
        continue
    if s == b:
        if mn > s:
            mn = n
    else:
        q.append((s + 1, n + 1))
        q.append((s - 1, n + 1))
        q.append((s * 2, n + 1))
print(mn)