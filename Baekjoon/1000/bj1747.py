import math

n = int(input())
is_prime = [True] * (1_000_001)
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(1_000_001)) + 1):
    if is_prime[i]:
        for j in range(i * i, 1_000_001, i):
            is_prime[j] = False

sosu = [i for i in range(2, 1_000_001) if is_prime[i]]
if n == 1: n = 2
if n >= 10 or n not in [2, 3, 5, 7]:
    n = n // 2 * 2 + 1 - 2
else:
    print(n)
    exit(0)
while True:
    n += 2
    t = True
    for i in sosu:
        # print(n, i)
        if i ** 2 > n:
            break
        if n % i == 0:
            t = False
            break
    if t:
        pa = True
        s = list(str(n))
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                pa = False
        if pa:
            print(n)
            break
        else:
            sosu.append(n)
            continue
