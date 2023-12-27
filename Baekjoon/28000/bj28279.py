import sys
from collections import deque
q = deque()

def isEmpty():
    if len(q) == 0:
        return True
    return False

for _ in range(int(sys.stdin.readline())):
    inp = sys.stdin.readline().strip()
    result = ""

    if len(inp.split()) == 1:
        if not isEmpty() and inp == '4':
            result = q.pop()
        elif not isEmpty() and inp == '3':
            result = q.popleft()
        elif inp == '5':
            result = len(q)
        elif inp == '6':
            result = int(isEmpty())
        elif isEmpty():
            result = -1
        elif inp == '7':
            result = q[0]
        elif inp == '8':
            result = q[-1]

        sys.stdout.write(f"{result}\n")
    else:
        m = inp.split()[0]
        v = inp.split()[1]
        if m == '1':
            q.appendleft(v)
        elif m == '2':
            q.append(v)

    # print(q)