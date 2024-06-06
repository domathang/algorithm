board = [list(map(int, input().split())) for _ in range(19)]
move = [[0, 1], [1, 0], [1, 1], [-1, 1]]
for i in range(19):
    for j in range(19):
        if board[i][j] in [1, 2]:
            color = board[i][j]
            for k in range(4):
                x = i
                y = j
                if x - move[k][0] > -1 and y - move[k][1] > -1 and x - move[k][0] < 19:
                    if board[x - move[k][0]][y - move[k][1]] == color:
                        continue
                for l in range(4):
                    if x + move[k][0] < 19 and y + move[k][1] < 19 and x + move[k][0] > -1:
                        if board[x + move[k][0]][y + move[k][1]] == color:
                            x += move[k][0]
                            y += move[k][1]
                        else: 
                            break
                    else:
                        break
                    # print(x, y)
                    if l == 3:
                        if x + move[k][0] < 19 and y + move[k][1] < 19 and x + move[k][0] > -1:
                            if board[x + move[k][0]][y + move[k][1]] != color:
                                # print("!!")
                                print(color)
                                print(f"{i+1} {j+1}")
                                exit(0)
                            else:
                                continue
                        else:
                            print(color)
                            print(f"{i+1} {j+1}")
                            exit(0)

print(0)