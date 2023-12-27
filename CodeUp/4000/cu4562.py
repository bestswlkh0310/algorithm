s = 1
for i in range(3):
    s *= int(input())
arr = [0] * 10
for i in list(map(int, list(str(s)))):
    arr[i] += 1
for i in arr:
    print(i)