import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

arr = [[0] * 10 for i in range(10)]

for i in range(10):
    arr[i][0] = 1
    arr[i][9] = 1
    arr[0][i] = 1
    arr[9][i] = 1

def mShow(cnt, ar, ch):
    print(end='[')
    for (i, id) in enumerate(ar):
        if i != 0:
            print(end=" ")
        print(end='[')
        for (idx, j) in enumerate(id):
            if idx == cnt - 1:
                if i == cnt - 1: print(end=f"{j}{ch}]")
                else: print(end=f"{j}{ch}]\n")
                break
            print(end=f"{j}{ch} ")
    print(']')
mShow(10, arr, '.')

arr = [[0] * 8 for i in range(8)]
for i in range(8):
    for j in range(8):
        if (i + j) % 2 != 0:
            arr[i][j] = 1
mShow(8, arr, '')
# print(arr)