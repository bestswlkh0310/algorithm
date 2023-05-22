a, b = map(int, input().split())
print(a // b, end=".")
if a // b != 0:
    a = a % b
for i in range(1005):
    print(a*10//b, end="")
    a *= 10
    a %= b
