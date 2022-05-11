def solve(a, b, m):
    global arr, answer
    first = True
    for i in range(m):
        for j in range(m):
            if arr[a][b] != arr[a + i][b + j]:
                first = False
    if first:
        answer += arr[a][b]
        return

    answer += '('
    for i in range(a, a + m, m // 2):
        for j in range(b, b + m, m // 2):
            solve(i, j, m // 2)
    answer += ')'


n = int(input())
arr = [input() for _ in range(n)]

answer = ''

solve(0, 0, n)

print(answer)
