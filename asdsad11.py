for i in range(int(input())):
    inp = list(input())
    mn = -1
    mx = 0
    for j in range(len(inp)):
        for k in range(len(inp)):
            b = []
            for a in inp:
                b.append(a)
            b[k], b[j] = b[j], b[k]
            s = ""
            if b[0] != '0':
                for w in b:
                    s += w
            if s != "":
                if mn == -1 or mn > int(s): mn = int(s)
                if mx < int(s): mx = int(s)
    print(mn, mx)