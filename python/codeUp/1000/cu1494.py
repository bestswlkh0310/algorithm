# 1494 차이 배열 만들기
n, k = map(int, input().split())
arr = [0] * (n + 1)
hArr = [0] * (n + 1)
for i in range(k):
    a, b, u = map(int, input().split())
    arr[a - 1] += u
    arr[b] -= u
del arr[-1]
for i in arr:
    print(i, end=" ")
s = 0
print()
for i in arr:
    s += i
    print(s, end=" ")