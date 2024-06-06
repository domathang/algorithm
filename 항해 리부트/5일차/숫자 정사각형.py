n, m = map(int, input().split())
rectangle = [input() for _ in range(n)]
answer = 1
for i in range(n - 1):
    for j in range(m - 1):
        find_number = rectangle[i][j]
        for k in range(j + 1, m):
            # 같은 행에서 같은 숫자를 찾으면
            if find_number == rectangle[i][k]:
                if i + k - j < n and find_number == rectangle[i + k - j][j] and \
                    find_number == rectangle[i + k - j][k]:
                    answer = max(answer, (k-j+1)**2)       
print(answer)