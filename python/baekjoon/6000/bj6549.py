# import sys
# import math

# sys.setrecursionlimit(10**4)

# input = sys.stdin.readline

# def init_tree(node, s, e, d):
#     if s == e:
#         T[node] = (lst[s], d, lst[s])
#         return T[node]

#     lc = init_tree(node * 2, s, (s + e) // 2, d // 2)
#     rc = init_tree(node * 2 + 1, (s + e) // 2 + 1, e, math.ceil(d / 2))

#     mn = min([lc[0], rc[0]])

#     T[node] = (mn, d, max(T[node][2], mn * d))
#     return T[node]
    

# def get_min(node, s, e, s1, e1):
#     # 겹치지 않음
#     if s > e1 or e < s1: return (1_000_000_001, 0, 0)

#     # 포함 됨 -> 이미 존재함
#     if s >= s1 and e <= e1: return T[node]

#     lc = get_min(node * 2, s, (s + e) // 2, s1, e1)
#     rc = get_min(node * 2 + 1, (s + e) // 2 + 1, e, s1, e1)

#     return max([lc[2], rc[2]])

# while True:
#     lst = [*map(int, input().split())]
#     if len(lst) == 1 and lst[0] == 0: break
#     T = [(1_000_000_001, 0, 0) for _ in range(3000000)]

#     n = len(lst)

#     init_tree(1, 0, n - 1, n)

#     print([i for i in T if i != (1_000_000_001, 0, 0)])

#     print(get_min(1, 0, n - 1, 0, n - 1))