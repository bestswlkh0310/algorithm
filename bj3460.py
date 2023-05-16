for t in range(int(input())):
    n = int(input())
    s = []
    idx = 0
    while n != 0:
        if n % 2:
            print(idx, end=" ")
        s.append(n % 2)
        n //= 2
        idx += 1
