answer = 0
n, m = map(int, input().split())

visit = [False for _ in range(n + 1)]

arr = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, n+1):
    if not visit[i]:
        q = []
        q += arr[i]
        f = 0
        r = len(q)
        while f < r:
            num = q[f]
            f += 1
            if not visit[num]:
                visit[num] = True
                q += arr[num]
                r += len(arr[num])
        answer += 1

print(answer)
