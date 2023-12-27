n, m = map(int, input().split())
is_prime = [True] * int(m ** 0.5+1)
is_prime[0] = is_prime[1] = False

nono = [True] * (m - n + 1)

for i in range(2, int(m ** 0.5) + 1):
    if is_prime[i]:
        if n % (i ** 2) == 0:
            nono[0] = 0
        k = n // (i ** 2) + 1
        while n <= i ** 2 * k <= m:
            nono[i ** 2 * k - n] = False
            k += 1
        for j in range(i * i, int(m ** 0.5)+1, i):
            is_prime[j] = False
print(nono.count(True))
