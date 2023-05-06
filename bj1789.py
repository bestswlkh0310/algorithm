# 1789 - 수들의 합
n = int(input())
s = 0
cnt = 0
for i in range(1, n + 1):
    s += i
    cnt += 1
    if s > n:
        break
if n != 1: print(cnt - 1)
else: print(1)