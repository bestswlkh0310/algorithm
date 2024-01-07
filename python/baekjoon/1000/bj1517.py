n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(n - i - 1):
        if lst[j + 1] < lst[j]:
            lst[j + 1], lst[j] = lst[j], lst[j + 1]
            cnt += 1

print(cnt)