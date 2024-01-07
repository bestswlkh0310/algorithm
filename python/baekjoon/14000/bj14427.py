import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        T[node] = lst[s]
        return T[node]
    
    lc = init_tree(node * 2, s, (s + e) // 2)
    rc = init_tree(node * 2 + 1, (s + e) // 2 + 1, e)

    if lc[0] < rc[0]:
        T[node] = lc
    elif lc[0] == rc[0] and lc[1] < rc[1]:
        T[node] = lc
    else:
        T[node] = rc
    return T[node]


def sub_sum(node, s, e, s1, e1):
    # 겹치지 않음
    if s > e1 or e < s1: return [1_000_000_001, -1]

    # 포함 됨 -> 이미 존재함
    if s >= s1 and e <= e1: return T[node]

    lc = sub_sum(node * 2, s, (s + e) // 2, s1, e1)
    rc = sub_sum(node * 2 + 1, (s + e) // 2 + 1, e, s1, e1)

    if lc[0] < rc[0]:
        return lc
    elif lc[0] == rc[0] and lc[1] < rc[1]:
        return lc
    else:
        return rc

def update(node, s, e, idx, c):
    if idx < s or idx > e: return

    if s == e:
        T[node] = c
        return

    update(node * 2, s, (s + e) // 2, idx, c)
    update(node * 2 + 1, (s + e) // 2 + 1, e, idx, c)
    lc = T[node * 2]
    rc = T[node * 2 + 1]
    if lc[0] < rc[0]:
        T[node] = lc
    elif lc[0] == rc[0] and lc[1] < rc[1]:
        T[node] = lc
    else:
        T[node] = rc

n = int(input())
lst = [[*(reversed(i))] for i in enumerate([*map(int, input().split())])]
T = [[1_000_000_001, -1] for _ in range(3000000)]

init_tree(1, 0, n - 1)

for _ in range(int(input())):
    inp = [*map(int, input().split())]

    if len(inp) == 1:
        print(sub_sum(1, 0, n - 1, 0, n - 1)[1] + 1)
    else:
        a, b, c = inp
        b -= 1
        lst[b][0] = c
        update(1, 0, n - 1, b, lst[b])