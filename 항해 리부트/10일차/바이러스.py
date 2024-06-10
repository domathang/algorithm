n = int(input())
m = int(input())
roads = [[] for _ in range(n+1)]
check = [0] * (n+1)
check[1] = 1
for i in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)
q = [1]
answer = 0
while q:
    p = q.pop(0)
    for j in roads[p]:
        if check[j] == 0:
            q.append(j)
            check[j] = 1
            answer += 1
print(answer)
