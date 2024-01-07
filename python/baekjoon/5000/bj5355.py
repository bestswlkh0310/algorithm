# 5355 - 화성 수학
for i in range(int(input())):
    lst = input().split()
    n = float(lst[0])
    del lst[0]
    for j in lst:
        if j == '@':
            n *= 3
        elif j == '%':
            n += 5
        elif j == '#':
            n -= 7
    print("%.2f" %n)