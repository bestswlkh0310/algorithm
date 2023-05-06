# 5063 - TGN
for q in range(int(input())):
    a, b, c = map(int, input().split())
    s = b - c
    if a < s: print("advertise")
    elif a == s: print("does not matter")
    else: print("do not advertise")