str = input()
while str.find("()") != -1:
    str = str.replace("()", "")
if str.find("(") != -1 or str.find(")") != - 1:
    print("bad")
else:
    print("good")
