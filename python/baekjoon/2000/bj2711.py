for i in range(int(input())):
    idx, s = input().split()
    idx = int(idx) - 1
    s = list(s)
    del s[idx]
    print("".join(s))