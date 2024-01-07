n = int(input())
arr = [[*map(int, list(input()))] for _ in range(n)]

def A(i, x1, y1, x2, y2):
    v = i // 2
    if i == 0:
        return
    s = sum([sum([arr[j][i] for j in range(y1, y2)]) for i in range(x1, x2)])
    
    if s == (x2 - x1) * (y2 - y1):
        print(end='1')
        return
    elif s == 0:
        print(end='0')
        return
    print(end='(')
    A(v, x1, y1, x2 - (x2 - x1) // 2, y2 - (y2 - y1) // 2)
    A(v, x1 + v, y1, x2, y2 - (y2 -y1) // 2)
    A(v, x1, y1 + v, x2 - (x2 - x1) // 2, y2)
    A(v, x1 + v, y1 + v, x2, y2)
    print(end=')')

A(n, 0, 0, n, n)
