for i in range(int(input())):
    n = int(input())
    s = 0
    for j in range(1, n + 1, 2):
        s += j
    print(s)