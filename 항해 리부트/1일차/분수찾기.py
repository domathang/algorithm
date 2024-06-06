x = int(input())
i, cnt = 2, 1
# i: 대각선 한 줄, cnt: 칸 하나마다 1씩 올라가는 수
while True:
    # c: 대각선 한줄마다 초기화되는 수
    c = 0
    for j in range(1, i):
        c += 1
        if cnt == x:
            if i % 2 == 1:
                print(f"{c}/{i-c}")
            else:
                print(f"{i-c}/{c}")
            exit(0)
        cnt += 1
    i += 1