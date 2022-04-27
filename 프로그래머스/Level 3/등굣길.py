def solution(m, n, puddles):
    arr = [[0] * (n+1) for _ in range(m+1)]
    arr[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if i + j != 2 and [i, j] not in puddles:
                arr[i][j] = (arr[i-1][j] + arr[i][j-1]) % 1000000007

    return arr[m][n]


print(solution(4, 3, [[2, 2]]))
