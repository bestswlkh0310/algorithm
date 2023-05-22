lst = list(input())
lst.reverse()
s = 0
for (idx, i) in enumerate(lst):
    s += int(i) * 2 ** idx
r = []
while s != 0:
    r.append(str(s % 8))
    s //= 8
r.reverse()
print("".join(r))