
n = int(input())
cnt = 0

def show(ar):
    ne = [['_'] * n for i in range(n)]
    for i in ar:
        ne[i[1]][i[0]] = '*'
    for i in ne:
        for j in i:
            print("%2c"%j,end="")
        print()
    print()
def A(ar, n1):
    global cnt
    if n1 == n:
        # show(ar)
        cnt += 1
        return
    for i in range(n):
        for j in range(n):
            t = True
            for (y, x) in ar:
                if i == y or j == x or i + j == y + x or i - j == y - x:
                    t = False
                    break
            if t:
                newArr = [(y1, x1) for (y1, x1) in ar]
                newArr.append((i, j))
                A(newArr, n1 + 1)


for i in range(n):
    for j in range(n):
        A([(i, j)], 1)

print(cnt)