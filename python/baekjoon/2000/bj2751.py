import sys

n = int(sys.stdin.readline())
arr = [0 for i in range(-1000000, 1000004)]
for i in range(n):
    arr[(int(sys.stdin.readline())) + 1000000] += 1
for i in range(0, 2000001):
    for j in range(arr[i]):
        sys.stdout.write(str(i - 1000000) + "\n")

# def quickSort(start, end):
#     if start >= end: return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and arr[left] <= arr[pivot]: left += 1
#         while right > start and arr[right] >= arr[pivot]: right -= 1
#         if left > right: arr[right], arr[pivot] = arr[pivot], arr[right]
#         else: arr[right], arr[left] = arr[left], arr[right]
#     quickSort(start, right - 1)
#     quickSort(right + 1, end)
# quickSort(0, n - 1)

# def quickSort(ar):
#     if len(ar) <= 1: return ar
#     pivot = ar[0]
#     tail = ar[1:]
#     leftSide = [x for x in tail if x <= pivot]
#     rightSide = [x for x in tail if x > pivot]
#     return quickSort(leftSide) + [pivot] + quickSort(rightSide)
# arr = quickSort(arr)
#
# for i in arr:
#     sys.stdout.write(str(i))