import heapq
n = int(input())
heap = []
minus_heap = []
for i in range(n):
    x = int(input())
    if x != 0:
        if x > 0:
            heapq.heappush(heap, x)
        else:
            heapq.heappush(minus_heap, -x)
    else:
        if not (heap or minus_heap):
            print(0)
            continue
        elif not heap:
            b = heapq.heappop(minus_heap)
            print(-b)
        elif not minus_heap:
            a = heapq.heappop(heap)
            print(a)
        else:
            a = heapq.heappop(heap)
            b = heapq.heappop(minus_heap)
            if a >= b:
                print(-b)
                heapq.heappush(heap, a)
            elif a < b:
                print(a)
                heapq.heappush(minus_heap, b)

