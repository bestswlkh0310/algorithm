i = 0
while True:
    i += 1
    inp = input()
    if inp == "0": break
    r, w, h = map(int, inp.split())
    r1 = ((w ** 2 + h ** 2) ** 0.5) / 2
    if r < r1:
        print(f"Pizza {i} does not fit on the table.")
    else:
        print(f"Pizza {i} fits on the table.")