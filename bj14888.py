import sys
n1 = int(input())
arr1 = list(map(int, input().split()))
s = list(map(int, input().split()))
mx = -9999999999999999999999999
mn = sys.maxsize


def A(arr, s, n):
    if n == n1 - 1:
        global mx, mn
        mx = max(mx, arr[-1])
        mn = min(mn, arr[-1])
        return
    for (idx, j) in enumerate(s):
        if j > 0:
            newArr = arr[:]
            newS = s[:]
            newS[idx] -= 1
            if idx == 0:
                newArr[n + 1] = arr[n] + arr[n + 1]
                A(newArr, newS, n + 1)
            elif idx == 1:
                newArr[n + 1] = arr[n] - arr[n + 1]
                A(newArr, newS, n + 1)
            elif idx == 2:
                newArr[n + 1] = arr[n] * arr[n + 1]
                A(newArr, newS, n + 1)
            else:
                newArr[n + 1] = int(arr[n] / arr[n + 1])
                A(newArr, newS, n + 1)
A(arr1, s, 0)
print(mx)
print(mn)