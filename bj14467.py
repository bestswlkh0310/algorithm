arr = [[-1, 0] for i in range(11)]
for i in range(int(input())):
    a, b = map(int, input().split())
    if arr[a][0] == -1 or arr[a][0] != bool(b):
        arr[a][0] = bool(b)
        arr[a][1] += 1
mx = 0
for i in range(11):
    if arr[i][1] > mx:
        mx = arr[i][1]
print(mx)