from heapq import heapify, heappop, heappush

t = int(input())
for i in range(t):
    k = int(input())
    heap = list(map(int, input().split()))
    heapify(heap)
    total = 0
    while len(heap) > 1:
        p1 = heappop(heap)
        p2 = heappop(heap)
        _sum = p1 + p2
        total += _sum
        heappush(heap, _sum)
    print(total)
