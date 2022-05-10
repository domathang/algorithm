def solve(x, y, m):
    global arr, cnt
    first_one = arr[x][y]

    if m == 1:
        cnt[first_one] += 1
        return

    go = False

    for i in range(m):
        for j in range(m):
            if arr[x + i][y + j] != first_one:
                go = True

    if not go:
        cnt[first_one] += 1
        return

    m3 = m // 3

    for i in range(x, x+m, m3):
        for j in range(y, y + m, m3):
            solve(i, j, m3)


n = int(input())
cnt = {-1: 0, 0: 0, 1: 0}
arr = [list(map(int, input().split())) for _ in range(n)]

solve(0, 0, n)

print(cnt[-1])
print(cnt[0])
print(cnt[1])
