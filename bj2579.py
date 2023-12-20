arr = []

for i in range(int(input())):
    n = int(input())
    if i == 0:
        arr.append((0, n))
        continue
    elif i == 1:
        arr.append((n + arr[0][1], n))
        continue
    
    arr.append((n + arr[-1][1], n + max(arr[-2])))


print(max(arr[-1]))
