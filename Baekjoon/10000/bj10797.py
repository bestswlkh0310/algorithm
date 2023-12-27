n = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if n == i % 10: cnt += 1
print(cnt)