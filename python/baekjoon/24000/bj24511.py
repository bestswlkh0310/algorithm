from collections import deque
I=lambda:[*map(int,input().split())]
_=I()
q = deque([i[1]for i in zip(I(),I()) if i[0] == 0][::-1])
N =I()[0]
print(' '.join([*map(str, ([*q][:N] + I())[:N])]))