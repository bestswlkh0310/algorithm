import math

n, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

def mul(arr1, arr2):
    result = [[0] * n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            s = sum(arr1[row][i] * arr2[i][col] for i in range(n))
            result[row][col] = s % 1000
    return result

for i in range(n):
    for j in range(n):
        arr[i][j] %= 1000

d = [arr]
for i in range(math.floor(math.log(k, 2))):
    if len(d) == 1:
        d.append(mul(d[0], d[0]))
    else: 
        d.append(mul(d[i], d[i]))

s = []

# print(d)

for (idx, i) in enumerate(list(reversed(list(map(int, list(str(bin(k)[2:]))))))):
    # print(i)
    if i == 1:
        # print(d[i])
        if len(s) == 0:
            s = d[idx]
        else:
            s = mul(s, d[idx])
    
for i in s:
    for j in i:
        print(j, end=' ')
    print()


