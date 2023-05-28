import sys

dic = dict()
for i in range(int(sys.stdin.readline())):
    a, b = sys.stdin.readline().split()
    if b[0] == "e":
        dic[a] = b
    else:
        del dic[a]
for i in reversed(sorted(dic.keys())):
    sys.stdout.write(f"{i}\n")