n = list(input())
n.reverse()
s = 0
for (idx, i) in enumerate(n):
    k = i
    if ord('A') <= ord(k) <= ord('F'):
        k = ord(k) - ord('A') + 10
    else:
        k = int(k)
    s += k * 16 ** (idx)
print(s)