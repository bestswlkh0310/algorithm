n = input()
l = len(n)
if l == 1:
    print(n)
    exit(0)
q = n[0]
n = n[1:]
s = (int(n) + 1) * l
for i in range(l):
    s += 9 * (10 ** (i - 1)) * i
print(int(s))

