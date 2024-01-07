import sys
input = sys.stdin.readline
while True:
    try:
        X = int(input()) * 10_000_000
        N = int(input())
        A = [*sorted([int(input()) for _ in range(N)])]
        left = 0
        right = N - 1
        t = True
        while left < right:
            V = A[left] + A[right]
            if V > X:
                right -= 1
            elif V < X:
                left += 1
            else:
                print('yes', A[left], A[right])
                t = False
                break
        if t:
            print('danger')
    except:
        break