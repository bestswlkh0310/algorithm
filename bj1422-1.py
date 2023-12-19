k, n = map(int, input().split())

lst = [int(input()) for _ in range(k)]

lst.sort()
lst.reverse()

mxL = n - k + 1

result = []

for _ in range(mxL):
    result.append(lst[0])
    

for i in range(1, n - mxL + 1):
    result.append(lst[i])

print(int(''.join(map(str, result))))