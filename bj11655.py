str = list(input())
result = []

for i in str:
    c = ord(i)
    if 65 <= c <= 90 or 97 <= c <= 122:
        if 90 >= c >= 78 or c > 109:
            c -= 26
        c += 13
    result.append(chr(c))
print("".join(result))