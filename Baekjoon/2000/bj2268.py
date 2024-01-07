import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        T[node] = lst[s]
        return T[node]

    lc = init_tree(node * 2, s, (s + e) // 2)
    rc = init_tree(node * 2 + 1, (s + e) // 2 + 1, e)

    T[node] = lc + rc
    return T[node]


def sub_sum(node, s, e, s1, e1):
    # 겹치지 않음
    if s > e1 or e < s1: return 0

    # 포함 됨 -> 이미 존재함
    if s >= s1 and e <= e1: return T[node]

    lc = sub_sum(node * 2, s, (s + e) // 2, s1, e1)
    rc = sub_sum(node * 2 + 1, (s + e) // 2 + 1, e, s1, e1)

    return lc + rc

def update(node, s, e, idx, diff):
    if idx < s or idx > e: return

    T[node] += diff

    if s != e:
        update(node * 2, s, (s + e) // 2, idx, diff)
        update(node * 2 + 1, (s + e) // 2 + 1, e, idx, diff)

n, m = map(int, input().split())
lst = [0 for _ in range(n)]
T = [0 for _ in range(3000000)]


init_tree(1, 0, n - 1)


for _ in range(m):
    a, b, c = map(int, input().split())

    if a == 1:
        b -= 1
        diff = c - lst[b]
        lst[b] = c
        update(1, 0, n - 1, b, diff)
    else:
        mn = min(b - 1, c - 1)
        mx = max(b - 1, c - 1)
        print(sub_sum(1, 0, n - 1, mn, mx))
