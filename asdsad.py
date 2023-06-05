# storey = int(input())
# d = []
# for i in range(len(str(storey)) + 1):
#     d.append(10 ** i)
#     d.append(-10 ** i)
# print(d)
# q = []
# v = [False] * (storey * 100)
# q.append((storey, 1))
# t = True
# r = 0
# while q and t:
#     k, n = q[0]
#     q = q[1:]
#     for i in d:
#         s = k + i
#         if s > storey * 10 or s < 0: continue
#         if s == 0:
#             r = n
#             t = False
#             break
#         if not v[s]:
#             q.append((s, n + 1))
#         v[s] = True
#
# print(r)



# ar = {
#     "123":12
# }
# for i in ar.values():
#     print(i)


# for i in range(100):
#     print(i % 5)

cnt = 0
num = int(input())
while True:
    print(cnt % num)
    cnt += 1
