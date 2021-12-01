def get_it(row):
    for i in range(len(row)):
        if row[i] != 0:
            x = row[i]
            row[i] = 0
            return x, row
    return 0, row

def solution(board, moves):
    answer = 0
    bucket = []
    board = [[board[j][i] for j in range(len(board[i]))] for i in range(len(board))]
    for i in moves:
        r, board[i-1] = get_it(board[i-1])

        if r != 0:
            if len(bucket) > 0 and bucket[-1] == r:
                bucket.pop()
                answer += 2
            else:
                bucket.append(r)

    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
               [1,5,3,5,1,2,1,4]))
