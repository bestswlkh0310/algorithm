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
        if not isEmpty() and inp == 'pop':
            result = q.popleft()
        elif inp == 'size':
            result = len(q)
        elif inp == 'empty':
            result = int(isEmpty())
        elif isEmpty():
            result = -1
        elif inp == 'front':
            result = q[0]
        elif inp == 'back':
            result = q[-1]

        sys.stdout.write(f"{result}\n")
    else:
        m = inp.split()[0]
        v = inp.split()[1]
        if m == 'push':
            q.append(v)

    # print(q)