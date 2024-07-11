# 최대 시간 복잡도 20C10 => O(184756)
# N개 중에 N/2개 뽑는 거임. (N은 20이하 짝수 AND 자연수)

from typing import List

R = []
# called = 0

def func(arr, result, N, k):
    # global R, called
    global R
    # called += 1

    for idx, i in enumerate(arr):
        if idx < k:
            continue
        newArr = arr[:]
        newResult = result[:]
        newResult[0] += i[0]
        newResult[1] += i[1]
        del newArr[idx]
        if len(newArr) > N // 2:
            func(newArr, newResult, N, idx)
        else:
            r = newResult[:]
            for j in newArr:
                r[0] -= j[0]
                r[1] -= j[1]
            lenResult = (r[0] ** 2 + r[1] ** 2) ** 0.5
            # print(end='result - ')
            # print(lenResult)
            R.append(lenResult)

for _ in range(int(input())):
    N = int(input())
    G = [[*map(int, input().split())] for _ in range(N)]
    func(arr=G, result=[0, 0], N=N, k=0)
    print(min(R))
    # print(f'callled - {called}')
    R = []
    called = 0