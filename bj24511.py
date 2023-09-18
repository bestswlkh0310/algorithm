n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

a = int(input())
arr3 = list(map(int, input().split()))
tmp = None
last = None
for i in arr3:
    for (idx, j) in enumerate(arr2):
        if arr1[idx] == 0:
            if tmp == None:
                tmp = arr2[idx]
                arr2[idx] = i
            else:
                arr2[idx] = tmp
                tmp = j
                