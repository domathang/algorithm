n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
INF = float("inf")
cost = [INF] * (n + 1)
for i in range(m):
    s, e, b = map(int, input().split())
    graph[s].append((e, b))
start_city, end_city = map(int, input().split())

q = [(0, start_city)]

while q:
    total_cost, idx = q.pop(0)
    if cost[idx] < total_cost:
        continue

    for adj, d in graph[idx]:
        if cost[adj] > total_cost + d:
            cost[adj] = total_cost + d
            q.append((total_cost + d, adj))

print(cost[end_city])
