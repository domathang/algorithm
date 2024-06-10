n, m = map(int, input().split())
roads = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)
s = int(input())
gomgom_check = [0] * (n+1)
for i in list(map(int, input().split())):
    gomgom_check[i] = 1
if gomgom_check[1] == 0:
    q = [1]
    while q:
        p = q.pop(0)
        if not roads[p]:
            print("yes")
            exit(0)
        for i in roads[p]:
            if gomgom_check[i] == 0:
                q.append(i)
print("Yes")