a, b, c = map(int, input().split())
a = a % b
r = 0
for i in range(c):
    a *= 10
    r = a // b
    a = a % b
print(r)