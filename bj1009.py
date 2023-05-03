num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    # b %= 4
    sum = a
    for j in range(b - 1):
        sum = sum * a % 10
    if sum == 0: print(10)
    else: print(sum)