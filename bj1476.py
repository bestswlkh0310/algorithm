e, s, m = map(int, input().split())
de, ds, dm = 1, 1, 1
s1 = 0

while True:
    if de == 16: de = 1
    if ds == 29: ds = 1
    if dm == 20: dm = 1
    s1 += 1
    if e == de and s == ds and m == dm:
        print(s1)
        break
    de += 1
    ds += 1
    dm += 1
