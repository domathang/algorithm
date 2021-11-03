def max_of_3(row, num):
    return max([row[i] for i in range(len(row)) if i != num])

def solution(land):
    d = [[0, 0, 0, 0] for _ in range(len(land))]
    d[0][0] = land[0][0]
    d[0][1] = land[0][1]
    d[0][2] = land[0][2]
    d[0][3] = land[0][3]

    for i in range(1, len(d)):
        for j in range(4):
            d[i][j] = max_of_3(d[i-1], j) + land[i][j]

    return max(d[len(land)-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
