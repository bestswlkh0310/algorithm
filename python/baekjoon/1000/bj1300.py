n = int(input()) # 4
k = int(input())

1
2
3
4
3
2
1

i = 1
s = 0

while i <= n and s < k:
    s += i
    i += 1

print(s)