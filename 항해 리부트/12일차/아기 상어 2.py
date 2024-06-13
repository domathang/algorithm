n, m = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
ny = [-1, -1, 0, 1, 1, 1, 0, -1]
nx = [0, 1, 1, 1, 0, -1, -1, -1]

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
            next_y = p[0] + ny[k]
            next_x = p[1] + nx[k]
            if safe(next_y, next_x) and visited[next_y][next_x] == 0:
                q.append((next_y, next_x, p[2] + 1))
                visited[next_y][next_x] = 1

answer = 0

for i in range(n):
    for j in range(m):
        if space[i][j] == 0:
            answer = max(answer, bfs(i, j))

print(answer)