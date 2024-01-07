import sys

n = int(input())
dic = {}
s1 = [0, 0]
s2 = [sys.maxsize, 0]
for i in range(n):
    a, b, c, d = input().split()
    b, c, d = map(int, [b, c, d])
    dic[a] = [b, c, d]
    s = b + c * 100 + d * 1000
    if s >= s1[0]:
        s1 = [s, a]
    if s <= s2[0]:
        s2 = [s, a]
print(s1[1])
print(s2[1])