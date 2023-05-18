while True:
    s = input()
    if s == '#':
        break
    s = list(s.upper())
    print(s.count("U") + s.count("I") + s.count("O") + s.count("A") + s.count("E"))