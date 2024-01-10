for _ in range(int(input())):
    m, n = map(int, input().split())
    
    q = m // n
    m = (m % n) * 10

    dividend = m
    dividend_list = []
    digit_list = []

    while True:
        if dividend in dividend_list: break
        dividend_list.append(dividend)
        digit = dividend // n
        dividend = (dividend % n) * 10
        digit_list.append(digit)

    idx = dividend_list.index(dividend)

    non_cyc = digit_list[:idx]
    cyc = digit_list[idx:]

    print(end=f'{q}.{"".join(map(str, non_cyc))}({"".join(map(str, cyc))})')
    print()