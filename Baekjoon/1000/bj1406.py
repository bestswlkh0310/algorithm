import sys
str = list(sys.stdin.readline())
n = int(sys.stdin.readline())
pos = len(str)
for i in range(n):
    inp = sys.stdin.readline().strip()
    if inp == "L":
        if pos > 0:
            pos -= 1
    elif inp == "D":
        if pos < len(str):
            pos += 1
    elif inp == "B":
        if pos > 0:
            del str[pos - 1]
            pos -= 1
    else:
        str.insert(pos, inp.split()[1])
        pos += 1
print("".join(str))