n = int(input())
s = [2]
d = [0 for _ in range(n + 1)]

mod = 123_456_789
for i in range(3, n + 1):
    t = True
    for j in s:
        if j ** 2 > i:break
        if not i % j:
            t = False
            break
    if t:
        s.append(i)

d[0] = 1
for j in s:
    for i in range(j, n + 1):
        d[i] = (d[i] + d[i - j]) % mod

print(d[-1])