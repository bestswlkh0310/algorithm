from collections import deque
import sys

n = int(sys.stdin.readline())

result = deque()

for _ in range(n):
    result.append(int(sys.stdin.readline()))

q = deque()
for i in range(n):
    q.append(i + 1)

stack = []

idx = 0

r = ""

while idx < n:
    if len(stack) != 0 and stack[-1] == result[idx]:
            q.append(stack.pop())
            r += '-\n'
            idx += 1
    else:
        if len(q) == 0:
            print('NO')
            sys.exit(0)
        stack.append(q.popleft())
        r += '+\n'

sys.stdout.write(r)