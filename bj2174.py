w, h = map(int, input().split())
n, m = map(int, input().split())
dic = {}
dic1 = {
    "N": (0, 1),
    "E": (1, 0),
    "W": (-1, 0),
    "S": (0, -1)
}
left = {
    "N": "W",
    "W": "S",
    "S": "E",
    "E": "N"
}
right = {
    "N": "E",
    "W": "N",
    "S": "W",
    "E": "S"
}

def check(id1, yy, xx):
    if not (0 <= yy < h and 0 <= xx < w):
        return -1
    for i in range(n):
        if i + 1 == id1: continue
        y0, x0, d = dic[i + 1]
        if y0 == yy and x0 == xx:
            return i + 1
    return 0

for i in range(n):
    x, y, d = input().split(); x, y = int(x) - 1, int(y) - 1
    dic[i + 1] = [y, x, d]
for _ in range(m):
    idx, mode, k = input().split(); idx, k = int(idx), int(k)
    for _ in range(k):
        if mode == "F":
            y1 = dic1[dic[idx][2]][1] + dic[idx][0]
            x1 = dic1[dic[idx][2]][0] + dic[idx][1]
            # print(y1, x1, dic[idx])
            chk = check(idx, y1, x1)
            if chk > 0:
                print(f"Robot {idx} crashes into robot {chk}")
                exit(0)
            elif chk == -1:
                print(f"Robot {idx} crashes into the wall")
                exit(0)
            else:
                dic[idx] = [y1, x1, dic[idx][2]]
        else:
            y1, x1, d = dic[idx]
            if mode == "L":
                dic[idx] = [y1, x1, left[d]]
            elif mode == "R":
                dic[idx] = [y1, x1, right[d]]
print("OK")