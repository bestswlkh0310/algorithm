import sys
str = sys.stdin.readline().rstrip()
while 'PPAP' in str:
    str = str.replace('PPAP', 'P')
print("PPAP" if str == "P" else "NP")



#


# import sys
# str = list(sys.stdin.readline()); del str[-1]
# if "".join(str) == "PPAP" or str == ["P"]:
#     print("PPAP")
# elif "".join(str).find("AA") != -1:
#     print("NP")
# elif str.count("P") == str.count("A") * 2 and len(str) >= 4 and str[0] == "P":
#     print("PPAP")
# else:
#     print("NP")
# PPAPPAPPAPPPAPPPAPPAPPAPPAPAPAP