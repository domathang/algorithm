n = int(input())
k = int(input())

a = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]

for i in range(k):
    x, y = list(map(int, input().split()))
    a[x].append(y)
    a[y].append(x)

s = [i for i in a[1]]
visit[1] = True

count = 0

while s:
    for i in s:
        visit[i] = True
        for j in a[i]:
            if not visit[j] and j not in s:
                s.append(j)
        count += 1
        s.remove(i)

print(count)
