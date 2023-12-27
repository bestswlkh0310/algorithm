a, b = input().split()
m = "F" if int(b[0]) % 2 == 0 else "M"
a = int(a)
y = None
if int(b[0]) <= 2:
    y = 113 - a // 10000
else:
    y = 13 - a // 10000
print(y, m)