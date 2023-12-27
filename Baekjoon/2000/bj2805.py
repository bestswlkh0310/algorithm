import sys
n, r = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

result = 0
end = max(lst)
start = 0
while start <= end:
    pivot = (start + end) // 2
    sum = 0
    for i in lst:
        if i > pivot:
            sum += i - pivot
    if sum >= r:
        result = pivot
        start = pivot + 1
    else:
        end = pivot - 1

print(result)