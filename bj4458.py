for i in range(int(input())):
    s = input()
    if 97 <= ord(s[0]) <= 122:
        print(chr(ord(s[0]) - 32), end="")
        print(s[1:])
    else:
        print(s)
