n, m = map(int, input().split())
n = 2 ** n
x, y = map(int, input().split())

t = None

def A(i, x1, y1, x2, y2, r, j):
    global t
    v = i // 2
    if i == 1:
        t = (y1, x1)
        return
    s = str(m)
    if s[j] == '2':
        A(v, x1, y1, x2 - (x2 - x1) // 2, y2 - (y2 - y1) // 2, r * 10 + 2, j + 1)
    elif s[j] == '1':
        A(v, x1 + v, y1, x2, y2 - (y2 -y1) // 2, r * 10 + 1, j + 1)
    elif s[j] == '3':
        A(v, x1, y1 + v, x2 - (x2 - x1) // 2, y2, r * 10 + 3, j + 1)
    else:
        A(v, x1 + v, y1 + v, x2, y2, r * 10 + 4, j + 1)

A(n, 0, 0, n, n, 0, 0)

def B(i, x1, y1, x2, y2, r):
    v = i // 2
    if x1 == x and y1 == y and x2 - 1 == x and y2 - 1 == y:
        return r

    if x < x2 - (x2 - x1) // 2:
        if y < y2 - (y2 - y1) // 2:
            return B(v, x1, y1, x2 - (x2 - x1) // 2, y2 - (y2 - y1) // 2, r * 10 + 2) # 2
        else:
            return B(v, x1, y1 + v, x2 - (x2 - x1) // 2, y2, r * 10 + 3) # 3
    else:
        if y < y2 - (y2 - y1) // 2:
            return B(v, x1 + v, y1, x2, y2 - (y2 -y1) // 2, r * 10 + 1) # 1
        else:
            return B(v, x1 + v, y1 + v, x2, y2, r * 10 + 4) # 4

x = t[1] + x
y = t[0] - y

if 0 <= x < n and 0 <= y < n:
    result = B(n, 0, 0, n, n, 0)
    print(result)
else:
    print(-1)

