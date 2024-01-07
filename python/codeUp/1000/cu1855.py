arr = [0] * 31
arr[0] = 0
arr[1] = 1
arr[2] = 1


def f(n):
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = f(n - 1) + f(n - 2)
        return arr[n]


print(f(int(input())))
