import sys
from collections import deque
input = sys.stdin.readline

s1 = list(input().strip('\n'))
s2 = deque()

n = int(input())
for _ in range(n):
    order = input().split()
    if order[0] == 'L' and s1:
        s2.appendleft(s1.pop())
    elif order[0] == 'D' and s2:
        s1.append(s2.popleft())
    elif order[0] == 'B' and s1:
        s1.pop()
    elif order[0] == 'P':
        s1.append(order[1])

for values in s1:
    print(values,end='')
for values in s2:
    print(values,end='')