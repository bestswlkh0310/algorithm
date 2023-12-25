n = int(input())

arr = [0] * max(4, n)

arr[0] = 1
arr[1] = 2
arr[2] = 4

def s(i):
    if i == 0: return 1
    if i == 1: return 2
    if i == 2: return 4
    if arr[i] != 0: return arr[i]
    arr[i] = (s(i - 1) + s(i - 2) + s(i - 3))
    return arr[i]

print(s(n - 1))
