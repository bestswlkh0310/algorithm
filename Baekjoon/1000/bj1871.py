for i in range(int(input())):
    a, b = input().split('-')
    b = int(b)
    a = list(a)
    a.reverse()
    s = 0
    for (idx, j) in enumerate(a):
        s += (ord(j) - ord('A')) * 26 ** idx
    if abs(s - b) <= 100:
        print("nice")
    else:
        print("not nice")
