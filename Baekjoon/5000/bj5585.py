n = 1000 -int(input())
a = [500, 100, 50, 10, 5, 1]
cnt = 0
while n != 0:
    for i in a:
        if n - i >= 0:
            n -= i
            cnt += 1
            break
print(cnt)