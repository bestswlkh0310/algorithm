arr = [[0] * 100 for i in range(100)]
visit = [[0] * 100 for i in range(100)]
for y in range(int(input())):
    a, b = map(int, input().split())
    for i in range(10):
        arr[a][b + i] += 1
        arr[a + 10][b + i] += 1
        arr[a + i][b] += 1
        arr[a + i][b + 10] += 1
    for i in range(8):
        for j in range(8):
            visit[a + i + 1][b + j + 1] = 1

for i in arr:
    for j in i:
        print(j, end="")
    print()

for i in visit:
    for j in i:
        print(j, end="")
    print()

# s = 0
# for i in range(100):
#     for j in range(100):
#         if arr[i][j] != 0 and visit[i][j] == 0:
#             s += 1
# print(s)

s = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] != 0 and visit[i][j] == 0:
            s += arr[i][j]
            print(f"{1}", end="")
        else:
            print("_", end="")
    print()
print(s)