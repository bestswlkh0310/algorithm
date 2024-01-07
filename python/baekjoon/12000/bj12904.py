str1 = list(input())
str2 = list(input())

while str1 != str2:
    if str2[-1] == "A":
        str2 = str2[0:-1]
    elif str2[-1] == "B":
        del str2[-1]
        str2.reverse()
    if len(str1) > len(str2):
        print(0)
        exit(0)
print(1)