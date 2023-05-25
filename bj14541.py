while True:
    n = int(input())
    if n == -1:
        break
    s = 0
    r = 0
    for i in range(n):
        a, b = map(int, input().split())
        r += a * (b - s)
        s = b
    print(r, "miles")