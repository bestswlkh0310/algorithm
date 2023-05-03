a = 100; b = 100

for i in range(int(input())):
    q, w = map(int, input().split())
    if q > w: b -= q
    if q < w: a -= w
print(a)
print(b)