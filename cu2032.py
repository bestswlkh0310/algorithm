n = int(input())
arr = []
l = 10 ** len(str(n))
for i in range(10):
    arr.append((n * 2) // l)
    n = (n * 2) % l
for i in arr:
    print(i,end="")
