import sys
n1 = int(sys.stdin.readline())
dic1 = {i:1 for i in list(map(int, sys.stdin.readline().split()))}
n2 = int(sys.stdin.readline())
for i in list(map(int, sys.stdin.readline().split())):
    try:
        sys.stdout.write(f"{dic1[i]} ")
    except:
        sys.stdout.write("0 ")