str = input().split(".")
result = ""
b = True
for i in str:
    length = len(i)
    if length % 2 != 0:
        b = False
        break
    for j in range(length // 4): result += "AAAA"
    for j in range((length - length // 4 * 4) // 2): result += "BB"
    result += "."
if b: print(result[0:-1])
else: print(-1)