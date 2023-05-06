for i in range(int(input())):
    a, b, c, d = map(int, input().split())

    dArr = []
    aArr = []
    s = []
    for i in range(1, abs(d) + 1):
        if d % i == 0: dArr.append(i)
        if a % i == 0: aArr.append(i)
    for i in dArr:
        for j in aArr:
            if i % j == 0:
                s.append(i // j)
                s.append(-(i // j))
    s = list(set(s))
    # print(s)
    x1 = 0
    for x in s:
        if a * (x ** 3) + b * (x ** 2) + c * x + d == 0:
            x1 = x
            break
    # print(x1)
    a1 = a
    b1 = a1 * x1 + b
    c1 = b1 * x1 + c
    # print(a1, b1, c1)
    x2 = (-b1 + (b1 ** 2 - 4 * a1 * c1) ** (1 / 2)) / (a1 * 2)
    x3 = (-b1 - (b1 ** 2 - 4 * a1 * c1) ** (1 / 2)) / (a1 * 2)
    result = [x1, x2, x3]
    # print(result)
    result = list(set(result))
    result.sort()
    for i in result:
        print("%.4f" % i, end=" ")
    print()