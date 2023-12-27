import sys

n = int(sys.stdin.readline())

dic = {}
cnt = 0
flag = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a == b:
        cnt += 1
        flag.append(a)
    elif a not in dic:
        dic[a] = b
    else:
        dic[a] = dic[a] if dic[a] < b else b
# for i in dic.items():
#     print(i)
# print(flag)
# print()
now = (-1, -1)
for (start, end) in sorted(dic.items()):
    if now[0] <= start and end < now[1]:
        now = (start, end)
    elif start >= now[1]:
        cn = 0
        for i in flag:
            if start < i < end:
                cn += 1
        # print(cn)
        if cn <= 1:
            now = (start, end)
            # print(now)
            cnt += 1
print(cnt)
# 4
# 3 3
# 2 3
# 1 3
# 2 2

# 4
# 7 7
# 1 7
# 1 7
# 1 1

# 5
# 1 100
# 100 300
# 99 101
# 199 300
# 199 201