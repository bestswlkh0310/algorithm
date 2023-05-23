n = int(input())
lst = list(map(int, input().split()))
cnt = 1
for i in range(n - 1):
    if lst[i] <= lst[i + 1]:
        cnt += 1
print(cnt)