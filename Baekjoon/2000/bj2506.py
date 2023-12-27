n = int(input())
a = 1
s = 0
lst = list(map(int, input().split()))
for k in lst:
    if k == 0:
        a = 1
    else:
        s += a
        a += 1
print(s)