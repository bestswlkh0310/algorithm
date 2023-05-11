import collections
lim, now, goal, a1, a2 = map(int, input().split())
result = -1
t = True

if a1 == 0 and a2 == 0 and (now != goal):
    result = -1
    t = False


visit = [False] * 1000001

q = collections.deque()
q.append((now, 0))
while q and t:
    (s, n) = q.popleft()
    if s == goal:
        result = n
        t = False
    elif 1 <= s <= lim and not visit[s]:
        visit[s] = True
        q.append((s + a1, n + 1))
        q.append((s - a2, n + 1))
if result == -1: print("use the stairs")
else: print(result)