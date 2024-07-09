n = int(input())
arr = [*sorted([int(input()) for _ in range(n)], reverse=True)]
# print(arr)

i = 0
r = 0

while i + 1 < n and arr[i] > 0 and arr[i + 1] >= 0:
    r += max(arr[i] + arr[i + 1], arr[i] * arr[i + 1])
    i += 2

if i < n and arr[i] > 0:
    r += arr[i]

j = n - 1

while j > 0 and arr[j] < 0 and arr[j - 1] <= 0:
    v = max(arr[j] + arr[j - 1], arr[j] * arr[j - 1])
    # print(f'v - {v}')
    r += v
    j -= 2
# print(r)
if 0 <= j and arr[j] < 0:
    r += arr[j]

# print(i, j)
print(r)