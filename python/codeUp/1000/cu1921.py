(n, k) = map(int, input().split())
arr = []
while n != 0:
    if n % k > 9:
        arr.append(chr(n % k + ord('A') - 10))
    else:
        arr.append(n % k)
    n //= k
arr.reverse()
for i in arr:
    print(end=f"{i}")