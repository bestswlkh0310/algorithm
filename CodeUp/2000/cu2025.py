a, b, c = input().split('/')
a = list(a)
b = list(b) + list(c)
a.sort()
b.sort()
if a == b:
    print("yes")
else:
    print("no")