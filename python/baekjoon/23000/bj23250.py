n, k = map(int, input().split())

cnt = 0
def move(n, x, y):
    global cnt
    if n > 1: move(n - 1, x, 6 - y - x)
    cnt += 1
    print(f'{cnt} {x} {y}')
    if n > 1: move(n - 1, 6 - x - y, y)

move(n, 1, 3)


# 홀수
# 1 => 1 3
# 3 => 3 2
# 5 => 2 1

# 2 => 1 2
# 4 => 1 3
# 6 => 2 3


# 짝수
# 1 => 1 2
# 3 => 2 3
# 5 => 3 1

# 2 => 1 3
# 4 => 1 2
# 6 => 3 2

if n % 2 == 1:
    if k % 2 == 1:
        v = (k // 2) % 3
        if v == 0: print(1, 3)
        elif v == 1: print(3, 2)
        elif v == 2: print(2, 1)
    else:
        v = (k // 2 - 1) % 3
        if v == 0: print(1, 2)
        elif v == 1: print(1, 3)
        elif v == 2: print(2, 3)
else:
    if k % 2 == 1:
        v = (k // 2) % 3
        if v == 0: print(1, 2)
        elif v == 1: print(2, 3)
        elif v == 2: print(3, 1)
    else:
        v = (k // 2 - 1) % 3
        if v == 0: print(1, 3)
        elif v == 1: print(1, 2)
        elif v == 2: print(3, 2)