import collections
n = int(input())
arr = [[False] * n for i in range(n)]
x, y = map(int, input().split())
q = collections.deque()
q.append((x, y))
dxy = (())
while q:
    (x, y) = q.popleft()
