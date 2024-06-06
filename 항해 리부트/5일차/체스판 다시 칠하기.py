n, m = map(int, input().split())
board = [input() for _ in range(n)]
min_ = 9999
for i in range(m-7):
    for j in range(n-7):
        # 첫칸 색깔 
        min_black, min_white = 0, 0

        for k in range(8):
            for l in range(8):
                # 0 2 4 6 번째 줄, 0 2 4 6 번째 칸 and 1 3 5 7 번째 줄 1 3 5 7 번째 칸
                if k % 2 == 0 and l % 2 == 0 or k % 2 == 1 and l % 2 == 1:
                    if board[j+k][i+l] != "B":
                        min_black += 1
                    else:
                        min_white += 1
                else:
                    if board[j+k][i+l] != "W":
                        min_black += 1
                    else:
                        min_white += 1
        min_ = min(min_, min_black, min_white)
print(min_)
