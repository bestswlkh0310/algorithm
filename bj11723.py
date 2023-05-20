import sys

lst = []
for i in range(int(sys.stdin.readline())):
    inp = sys.stdin.readline().split()
    if len(inp) == 2:
        inp[1] = int(inp[1])
        m, n = inp
        if m == "add":
            if n not in lst:
                lst.append(n)
        if m == "remove":
            if n in lst:
                lst.remove(n)
        if m == "check":
            if n in lst:
                print(1)
            else:
                print(0)
        if m == "toggle":
            if n in lst:
                lst.remove(n)
            else:
                lst.append(n)
    else:
        if inp[0] == "all":
            lst = [i for i in range(1, 21)]
        else:
            lst = []