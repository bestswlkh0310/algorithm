# -8 5 -3 2 -1 1 0 1 2 3 5 8 13 21 34 55

n = int(input())

if n < 0 and n % 2 == 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

a, b = 1, 1

if abs(n) == 1 or n == -2:
    print(1)
elif abs(n) == 0:
    print(0)
else:
    s = a + b
    for i in range(abs(n) - 2):
        s = (a + b) % 1_000_000_000
        a = b
        b = s

    print(s)