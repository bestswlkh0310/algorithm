# 1 <= k <= n 일떄 k, n의 서로소의 개수
# 오일러 피
# p[i] = p[i] - p[i] / k
import math
n = int(input())
arr = [i for i in range(n + 1)]
i = 2
while i < n ** 0.5:
    if i == arr[i]:
        k = arr[i]
        j = i
        while j <= n:
            arr[j] -= arr[j] // k
            j += k
    i += 1

print(arr[i] ** 2 - arr[i])
print(arr)

# n 의 약수 중 소수를 s라 할때
# n -= n // s

# 2 {3} 4 5 {6} 7 8 (9)
# => 2개
# (9 - 3) / 3
# (n - k) / k
# 1 2 3 4 5 6 7 8 9 10 11 12
#