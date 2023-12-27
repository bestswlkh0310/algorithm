num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    b = (b - 1) % 4 + 1
    sum = a
    for j in range(b - 1):
        sum = sum * a % 10
    print((sum - 1) % 10 + 1)
# 1 1 1 1 1
# 2 4 8 6 2
# 3 9 7 1 3
# 4 6 4 6 4
# 5 0 5 0 5
# 6 6 6 6 6
# 7 9 3 1 7
# 8 4 2 6 8
# 9 1 9 1 9