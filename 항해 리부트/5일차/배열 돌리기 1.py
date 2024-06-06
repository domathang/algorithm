n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [[0] * m for _ in range(n)]
rr = min(n, m) // 2

for _ in range(r):
    start_x, start_y = 0, 0
    end_x, end_y = m-1, n-1

    for i in range(rr):
        # 윗줄
        for j in range(start_x, end_x):
            arr2[start_y][j] = arr[start_y][j+1]
        # 왼쪽
        for j in range(start_y+1, end_y+1):
            arr2[j][start_x] = arr[j-1][start_x]
        # 아래
        for j in range(start_x+1, end_x+1):
            arr2[end_y][j] = arr[end_y][j-1]
        # 오른쪽
        for j in range(start_y, end_y):
            arr2[j][end_x] = arr[j+1][end_x]

        start_x += 1
        start_y += 1
        end_x -= 1
        end_y -= 1

    arr = [i[:] for i in arr2]

for i in arr:
    print(*i)