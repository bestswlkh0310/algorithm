n = int(input())
result = 0
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        result += b
    else:
        result += b - (b // a) * a
print(result)
