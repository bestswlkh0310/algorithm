import collections
import sys

a, b = map(int, input().split())
if a == b:
    print(0)
    exit(0)
mn = sys.maxsize

visit = [0] * 1000000

q = collections.deque()
q.append((a + 1, 1))
q.append((a - 1, 1))
q.append((a * 2, 1))
t = True
while q and t:
    (s, n) = q.popleft()
    if s == b:
        mn = n
        t = False
    elif 0 <= s < 1000000 and visit[s] == 0:
        visit[s] = n
        q.append((s + 1, n + 1))
        q.append((s - 1, n + 1))
        q.append((s * 2, n + 1))
print(mn)