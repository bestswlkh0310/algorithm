i = 0
while True:
    i += 1
    inp = int(input())
    if inp == 0: break
    inp *= 3
    if inp % 2 == 0:
        print("%d. %s " %(i, "even"), end="")
        inp //= 2
    else:
        print("%d. %s " %(i, "odd"), end="")
        inp = (inp + 1) // 2
    inp *= 3
    inp //= 9
    print(inp)