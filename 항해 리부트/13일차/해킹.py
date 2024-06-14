from heapq import *

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    adj_lst = [[] for _ in range(n+1)]
    INF = float('inf')
    infection = [INF] * (n+1)
    for i in range(d):
        a, b, s = map(int, input().split())
        adj_lst[b].append((a, s))
    
    q = [(0, c)]
    infection[c] = 0

    while q:
        seconds, idx = heappop(q)
        if infection[idx] < seconds:
            continue

        for adj, d in adj_lst[idx]:
            if infection[adj] > seconds + d:
                infection[adj] = seconds + d
                heappush(q, (infection[adj], adj))
    
    infection = [infection[i] for i in range(1, n+1) if infection[i] < INF]
    print(f"{len(infection)} {max(infection)}")