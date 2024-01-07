a, b = map(int, input().split())
mx = 0
idx = 0
for i in range(a, b + 1):
    cnt = 1
    s = i
    while s != 1:
        cnt += 1
        if s % 2 == 0:
            s //= 2
        else:
            s = s * 3 + 1
    if cnt > mx:
        idx = i
        mx = cnt
print(idx, mx)
