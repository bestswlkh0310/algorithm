result = 0


def A(n):
    global result
    if n <= 3:
        result += 1
        if n == 2:
            A(n - 1)
        if n == 3:
            A(n - 1)
            A(n - 2)
    else:
        A(n - 1)
        A(n - 2)
        A(n - 3)
inp = int(input())
A(inp)
print(result % 1000)
