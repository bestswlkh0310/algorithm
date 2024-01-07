c = False
for i in range(5):
    str = input()
    if "FBI" in str:
        print(i + 1, end=" ")
        c = True
if not c:
    print("HE GOT AWAY!")