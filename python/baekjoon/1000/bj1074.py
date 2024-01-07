n, c, r = map(int, input().split())
sum = 0

def A(i, x, y):
    global sum
    v = 2 ** i // 2
    if i <= 1:
        return
    if x <= r < v + x:
        if y <= c < v + y:
            sum += v ** 2 * 0
            A(i - 1, x, y)
        else:
            sum += v ** 2 * 2
            A(i - 1, x, v + y)
    else:
        if y <= c < v + y:
            sum += v ** 2 * 1
            A(i - 1, x + v, y)
        else:
            sum += v ** 2 * 3
            A(i - 1, x + v, y + v)
        
A(n, 0, 0)

print(sum + (1 if r % 2 == 1 else 0) + (2 if c % 2 == 1 else 0))