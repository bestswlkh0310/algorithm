n = int(input())
lst = list(map(int, input().split()))
k = int(input())
arr = [0 for _ in range(n)] # 엄마는 True

pr = lst[k]

# 엄마 삭제
for (idx, i) in enumerate(lst):
    if i != -1:
        arr[i] += 1

import collections
# print(arr)

q = collections.deque()
q.append(k)
arr[k] += 1 # fix

# 탐색
while q:
    p = q.popleft()
    for (idx, i) in enumerate(lst):
        if i == p:
            arr[idx] = None
            q.append(idx)
# print(arr)
cnt = 0
for (idx, i) in enumerate(arr):
    # print('t', idx, i)
    if i == 0:
        cnt += 1
    if idx == pr and i == 1:
        cnt += 1
        
print(cnt)

# 2
# -1 0
# 1

# 9
# -1 0 0 5 2 4 4 6 6
# 4
# => 2