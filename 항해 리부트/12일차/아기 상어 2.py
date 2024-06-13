n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def safe(i, j):
    if -1 < i < n and -1 < j < m:
        return True
    return False


def bfs(i, j):
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    q = [(i, j, 0)]
    while q:
        p = q.pop(0)
        if space[p[0]][p[1]] == 1:
            return p[2]
        for k in range(8):
            ny = p[0] + dy[k]
            nx = p[1] + dx[k]
            if safe(ny, nx) and visited[ny][nx] == 0:
                q.append((ny, nx, p[2] + 1))
                visited[ny][nx] = 1

answer = 0

for i in range(n):
    for j in range(m):
        if space[i][j] == 0:
            answer = max(answer, bfs(i, j))

print(answer)