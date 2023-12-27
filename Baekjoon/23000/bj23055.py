inp = int(input())
arr = [[' '] * inp for i in range(inp)]
for i in range(inp):
    arr[i][0] = "*"
    arr[0][i] = "*"
    arr[i][inp - 1] = "*"
    arr[inp - 1][i] = "*"
    arr[i][i] = "*"
    arr[i][inp - i - 1] = "*"
for i in range(inp):
    for j in range(inp):
        print(arr[i][j], end="")
    print()
