arr = [i for i in range(1, 21)]

for i in range(10):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    for j in range((b - a) // 2 + 1):
        arr[a + j], arr[a + (b - a) - j] = arr[a + (b - a) - j], arr[a + j]
for i in arr:
    print(end=f"{i} ")
