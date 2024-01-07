open = ['[', '{', '(']
close = [']', '}', ')']
sss = [';', ',']

for i in range(int(input())):
    t = True
    inp1 = input().split()
    inp2 = input().split()

    str1 = list(" ".join(inp1))
    str2 = list(" ".join(inp2))
    for (idx, k) in enumerate(str1):
        if k in open or k in close or k in sss or k == '.' or k == ':':
            try:
                if str1[idx - 1] == ' ':
                    str1[idx - 1] = '!'
                if str1[idx + 1] == ' ':
                    str1[idx + 1] = '!'
            except:
                pass
    for (idx, k) in enumerate(str2):
        if k in open or k in close or k in sss or k == '.' or k == ':':
            try:
                if str2[idx - 1] == ' ':
                    str2[idx - 1] = '!'
                if str2[idx + 1] == ' ':
                    str2[idx + 1] = '!'
            except:
                pass

    str1 = "".join([i for i in str1 if i != '!'])
    str2 = "".join([i for i in str2 if i != '!'])
    if len(str1.split()) != len(str2.split()):
        t = False
    else:
        for j in range(len(str1)):
            a = str1[j].upper()
            b = str2[j].upper()
            if not ((a in open and b in open) or (a in close and b in close) or (a in sss and b in sss)
                    or (a.isupper() and b.isupper()) or (a.isdigit() and b.isdigit()) or (a == '.' and b == '.') or (
                            a == ':' and b == ':') or (a == ' ' and b == ' ')):
                t = False
    if t:
        print(f"Data Set {i + 1}: equal\n")
    else:
        print(f"Data Set {i + 1}: not equal\n")
