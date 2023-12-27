from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

result = deque([int(input()) for _ in range(n)])
stack = deque()

i = 1
idx = 0
r = ""

while idx < n:
    if i > n + 1:
        print('NO')
        exit(0)
    if len(stack) != 0 and stack[-1] == result[idx]:
            stack.pop()
            r += '-\n'
            idx += 1
    else:
        # if i == 1:
        #     print('NO')
        #     sys.exit(0)
        stack.append(i)
        i += 1
        r += '+\n'
sys.stdout.write(r)