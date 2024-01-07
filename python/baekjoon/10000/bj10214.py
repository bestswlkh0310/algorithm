for i in range(int(input())):
    a = 0; b = 0
    for j in range(9):
        q, w = map(int, input().split())
        a += q
        b += w
    if a > b: print("Yonsei")
    elif a < b: print("Korea")
    else: print("Draw")