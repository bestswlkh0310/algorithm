# 7567 - 그릇
str = list(input())
now = str[0]
s = 0
for i in str:
    if now == i: s += 5
    else: s += 10
    now = i
print(s + 5)