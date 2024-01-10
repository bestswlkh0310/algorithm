g = int(input())

t = True
for i in range(1, g):
    if i ** 2 >= g:
        v = (i ** 2 - g) ** 0.5
        if v > 0 and v % 1 == 0.0:
            print(i)
            t = False

if t:
    print(-1)