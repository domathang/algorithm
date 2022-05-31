def dfs(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        x = dfs(a, b // 2, c) % c
        return (x * x) % c
    else:
        x = dfs(a, b // 2, c) % c
        return (x * x) % c * a % c


A, B, C = map(int, input().split())

print(dfs(A, B, C))
