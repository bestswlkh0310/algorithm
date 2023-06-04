n, k = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i, n):
        if k == sum(lst[i:j + 1]) and len(lst[i:j + 1]) > 0:
            cnt += 1

print(cnt)