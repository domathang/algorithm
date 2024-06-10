n, m, k, x = map(int, input().split())
roads = [[] for _ in range(n + 1)]
check = [0] * (n+1)
check[x] = 1
for i in range(m):
    a, b = map(int, input().split())
    if b not in roads[a]:
        roads[a].append(b)
    if a == x:
        check[b] = 1
q = roads[x]
for i in range(k-1):
    q_copy = q[:]
    q = []
    for j in q_copy:
        for l in roads[j]:
            if check[l] == 0:
                q.append(l)
                check[l] = 1
if q:
    q.sort()
    for i in q:
        print(i)
else:
    print(-1)
