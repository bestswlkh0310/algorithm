import sys
str = sys.stdin.readline()
while str.find("PPAP") != -1:
    print(str)
    idx = str.find("PPAP")
    str = str[:idx] + "P" + str[idx + 4:]
    print(str)
if str == "P":
    print("PPAP")
else:
    print("NP")