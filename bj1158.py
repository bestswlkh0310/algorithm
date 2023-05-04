a, b = map(int, input().split())
arr = [i + 1 for i in range(a)]
pos = 0
result = []
while arr:
    # print(arr, pos)
    for i in range(b - 1):
        pos += 1
        if pos >= len(arr):
            pos -= len(arr)
    try:
        result.append(arr[pos])
        del arr[pos]
    except:
        result.append(arr[0])
        break
print(end="<")
for i in range(len(result) - 1):
    print(f"{result[i]},",end=" ")
print(result[-1], end=">")