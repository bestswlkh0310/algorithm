n, s = map(int, input().split())

lst = list(map(int, input().split()))

idx1 = 0
idx2 = 0
sum = 0
mn = float("inf")

while not (idx1 == n and idx2 == n):
    if sum < s and idx2 < n:
        sum += lst[idx2]
        idx2 += 1
    elif sum >= s and idx1 < n:
        mn = min(mn, idx2 - idx1)
        sum -= lst[idx1]
        idx1 += 1
    elif idx1 < n:
        sum -= lst[idx1]
        idx1 += 1

if mn == float('inf'):
    print(0)
else:
    print(mn)
# 7 5
# 1 1 1 1 1 2 3
# 10 15
# 5 1 3 5 10 7 4 9 2 8
# 10 11
# 3 1 1 1 1 1 1 1 1 2
# 5 100
# 1 1 100 1 1