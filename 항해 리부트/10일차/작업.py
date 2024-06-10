n, m = map(int, input().split())
roads = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    roads[b].append(a)
x = int(input())

q = [x]
check = [0] * (n+1)
check[x] = 1
answer = 0
while q:
    p = q.pop(0)
    for i in roads[p]:
        if check[i] == 0:
            q.append(i)
            check[i] = 1
    answer += 1
print(answer-1)