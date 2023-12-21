lst = list(map(int, input()))

ar = []

while True:
    n = lst[0] * len(lst)
    if n in ar:
        print('FA')
        exit(0)
    ar.append(n)
    lst = list(map(int, (list(str(n)))))