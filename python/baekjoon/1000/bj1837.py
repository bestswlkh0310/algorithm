n, k = map(int, input().split())
if n % 2 == 0:
    if 2 < k:
        print("BAD", 2)
    else:
        print("GOOD")
    exit(0)
for i in range(3, n, 2):
    if n % i == 0:
        if i < k:
            print("BAD", i)
        else:
            print("GOOD")
        break