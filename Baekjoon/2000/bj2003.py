n, m = map(int, input().split())
lst = list(map(int, input().split()))
# 0 1 2 3 51 2 3

s = 0
e = 1
cnt = 0
l = len(lst)

while s <= e and s < l and e < l + 1:
    k = sum(lst[s:e])
    if k == m:
        cnt += 1
        s += 1
    if k < m:
        e += 1
    elif k > m:
        s += 1

print(cnt)