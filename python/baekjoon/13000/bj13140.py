n=int(input())

# hello
# world

for h in range(1, 10):
    for w in range(1, 10):
        for e in range(10):
            for l in range(10):
                for o in range(10):
                    for r in range(10):
                        for d in range(10):
                            v = [h, w, e, l, o, r, d]
                            if len(v) != len(set(v)): continue
                            hello=f'{h}{e}{l}{l}{o}'
                            world=f'{w}{o}{r}{l}{d}'
                            if int(hello) + int(world) == n:
                              print(" ", hello)
                              print("+", world)
                              print('-------')
                              print(str(n).rjust(7, ' '))
                              exit(0)


print('No Answer')