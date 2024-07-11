
R = [0 for _ in range(10)]

def calc(n, D):
    while n > 0:
        R[n % 10] += D
        n //= 10

S = 1
N = int(input())
D = 1
while S <= N:
    while S % 10 != 0 and S <= N:
        calc(S, D)
        S += 1

    if S > N: break
    while N % 10 != 9 and S <= N:
        calc(N, D)
        N -= 1

    cnt = (N // 10 - S // 10 + 1) * D
    for i in range(10):
        R[i] += cnt
    S //= 10
    N //= 10
    D *= 10

print(' '.join([*map(str, R)]))