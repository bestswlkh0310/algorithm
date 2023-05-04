a, b, c = map(int, input().split())
s = a * b - c
if s < 0:
    print(0)
else:
    print(s)