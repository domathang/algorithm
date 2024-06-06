n, m = map(int, input().split())


def dfs(suyeol, n1):
    if len(suyeol) == m:
        print(*suyeol)
        return
    for i in range(n1 + 1, n + 1):
        suyeol.append(i)
        dfs(suyeol, i)
        suyeol.pop()
dfs([], 0)
