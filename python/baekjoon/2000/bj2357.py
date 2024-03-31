import sys

sys.setrecursionlimit(10**4)

input = sys.stdin.readline

def init_tree(node, s, e):
    if s == e:
        T[node] = lst[s]
        T1[node] = lst[s]
        return (T[node], T1[node])

    lc = init_tree(node * 2, s, (s + e) // 2)
    rc = init_tree(node * 2 + 1, (s + e) // 2 + 1, e)

    T[node] = min([lc[0], rc[0]])
    T1[node] = max([lc[1], rc[1]])
    return (T[node], T1[node])


def get(node, s, e, s1, e1):
    # 겹치지 않음
    if s > e1 or e < s1: return (1_000_000_001, 1)

    # 포함 됨 -> 이미 존재함
    if s >= s1 and e <= e1: return (T[node], T1[node])

    lc = get(node * 2, s, (s + e) // 2, s1, e1)
    rc = get(node * 2 + 1, (s + e) // 2 + 1, e, s1, e1)

    return (min([lc[0], rc[0]]), max([lc[1], rc[1]]))

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]
T = [1_000_000_001 for _ in range(3000000)]
T1 = [1 for _ in range(3000000)]

init_tree(1, 0, n - 1)

for _ in range(m):
    b, c = map(int, input().split())

    mn, mx = get(1, 0, n - 1, b - 1, c - 1)

    print(mn, mx)