n, x = map(int, input().split())

mat = [tuple(map(int, input().split())) for _ in range(n)]

mat.sort(key=lambda y: y[0] - y[1], reverse=True)

answer = 0

for i in range(n):
    if x - 5000 >= (n-i-1) * 1000 and mat[i][0] > mat[i][1]:
        answer += mat[i][0]
        x -= 5000
    else:
        answer += mat[i][1]
        x -= 1000

print(answer)
