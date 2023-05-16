import collections

n = int(input())
arr1 = []
arr2 = []
for i in range(n):
    inp = list(input())
    arr1.append(inp)
    arr2.append(inp)

visit1 = [[False] * n for i in range(n)]
visit2 = [[False] * n for i in range(n)]

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if not visit1[i][j]:
            cnt1 += 1
            visit1[i][j] = True
            k = arr1[i][j]
            q = collections.deque()
            q.append((i, j))
            while q:
                (y, x) = q.popleft()
                for a in dxy:
                    mx = x + a[0]
                    my = y + a[1]
                    if 0 <= mx < n and 0 <= my < n and not visit1[my][mx] and arr1[my][mx] == k:
                        visit1[my][mx] = True
                        q.append((my, mx))
        if not visit2[i][j]:
            cnt2 += 1
            visit2[i][j] = True
            k = arr2[i][j]
            if k == 'R' or k == 'G':
                k = ['R', 'G']
            else:
                k = ['B']
            q = collections.deque()
            q.append((i, j))
            while q:
                (y, x) = q.popleft()
                for a in dxy:
                    mx = x + a[0]
                    my = y + a[1]
                    if 0 <= mx < n and 0 <= my < n and not visit2[my][mx] and arr2[my][mx] in k:
                        visit2[my][mx] = True
                        q.append((my, mx))

print(cnt1)
print(cnt2)