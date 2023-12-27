n = int(input()) + 1
s = []
while n:
    s.append(n % 2)
    n //= 2
s.reverse()
del s[0]
for i in s:
    print(7 if i == 1 else 4, end="")
