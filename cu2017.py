n, k = map(int, input().split())
s = []
if n == 0:
    print(0)
while n != 0:
    if n % k > 9:
        s.append(chr(ord('A') + n % k - 10))
    else:
        s.append(n % k)
    n //= k
s.reverse()
for i in s:
    print(i, end="")