n = int(input())
cnt = 0
for i in range(1234, n + 1):
    j = 1
    lst = list(map(int, list(str(i))))
    for k in lst:
        if k == j:
            j += 1
            if j == 5:
                cnt += 1
                break
print(cnt)
