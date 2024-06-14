dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
INF = float('inf')
problem = 1

while True:
    n = int(input())
    
    if n == 0: break
    
    cave = [list(map(int, input().split())) for _ in range(n)]

    min_rupee = [[INF] * n for _ in range(n)]
    min_rupee[0][0] = cave[0][0]

    q = [(0, 0, cave[0][0])]

    while q:
        y, x, cost = q.pop(0)
        if min_rupee[y][x] < cost:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 < ny < n and -1 < nx < n and min_rupee[ny][nx] > cost + cave[ny][nx]:
                min_rupee[ny][nx] = cost + cave[ny][nx]
                q.append((ny, nx, cost + cave[ny][nx]))
    
    print(f"Problem {problem}: {min_rupee[n-1][n-1]}")
    problem += 1


