for i in range(int(input())):
    s = int(input())
    for j in range(int(input())):
        a, b = map(int, input().split())
        s += a * b
    print(s)