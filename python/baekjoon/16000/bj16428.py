a, b = map(int, input().split())
if b > 0:
    print(a // b)
    print(a % b)
else:
    print(-(a // abs(b)))
    print(a % abs(b))