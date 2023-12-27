n = int(input())
cnt = 0
i = 1
while i < n:
    cnt += i * n + i
    i += 1

print(cnt)