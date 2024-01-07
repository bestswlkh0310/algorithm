import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    h1 = []  # 최소 힙
    h2 = []  # 최대 힙
    in_heap = set()  # 삭제된 값들을 추적하기 위한 set

    n = int(input())
    for _ in range(n):
        m, v = input().split()
        v = int(v)
        if m == 'I':
            heapq.heappush(h1, v)
            heapq.heappush(h2, -v)
            continue
        if v == -1 and len(h1) > 0:
            while h1:
                p = heapq.heappop(h1)
                if p not in in_heap:
                    in_heap.add(p)
                    break
        elif len(h1) > 0:
            while h2:
                p = -heapq.heappop(h2)
                if p not in in_heap:
                    in_heap.add(p)
                    break

    remaining_values = [x for x in h1 if x not in in_heap]
    if remaining_values:
        print(max(remaining_values), min(remaining_values))
    else:
        print('EMPTY')
