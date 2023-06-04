n = int(input())
cnt = 0
for i in range(1, n + 1):
    s = str(i)
    if len(s) == 1:
        cnt += 1
        continue
    f = int(s[0]) - int(s[1])
    t = True
    for j in range(len(s) - 1):
        if int(s[j]) - int(s[j + 1]) != f:
            t = False
            break
    if t:
        cnt += 1

print(cnt)