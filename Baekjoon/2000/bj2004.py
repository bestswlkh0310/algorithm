n, m = map(int, input().split())

def A(i): # n / (5) + n / (5 * 5) + n / (5 * 5 * 5))
    s = 0
    j = 1
    while 5 ** j <= 2_000_000_000:
        s += i // 5 ** j
        j += 1
    return s

print(A(n) - A(n - m + 1) - A(m))
