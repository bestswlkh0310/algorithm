n = list(input())
j = len(n)
s = 0
for i in n:
    s += int(i) * (10 * j)
    j -= 1
print(s)