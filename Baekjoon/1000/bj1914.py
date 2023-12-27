def move(n, x, y):
    if n > 1: move(n - 1, x, 6 - y - x)
    print(f'{x} {y}')
    if n > 1: move(n - 1, 6 - x - y, y)

n = int(input())

print(2 ** n - 1)
if n <= 20:
    move(n, 1, 3)
