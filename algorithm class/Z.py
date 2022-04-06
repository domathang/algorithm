N, r, c = list(map(int, input().split()))
answer = 0

def z(n, sx, sy, ex, ey):
    global r, c, answer
    if ex - sx == 1 and ey - sy == 1:
        if sx == r and sy == c:
            answer = n
        elif sx == r and ey == c:
            answer = n + 1
        elif ex == r and sy == c:
            answer = n + 2
        elif ex == r and ey == c:
            answer = n + 3
        return
    s = (ex - sx + 1) ** 2 // 4
    if (ex + sx) // 2 >= r and (ey + sy) // 2 >= c:
        z(n, sx, sy, (ex + sx) // 2, (ey + sy) // 2)
    elif (ex + sx) // 2 >= r and ey >= c:
        z(n + s, sx, sy + (ey - sy) // 2 + 1, (ex + sx) // 2, ey)
    elif ex >= r and (ey + sy) // 2 >= c:
        z(n + 2 * s, (ex + sx) // 2 + 1, sy, ex, (ey + sy) // 2)
    elif ex >= r and ey >= c:
        z(n + 3 * s, (ex + sx) // 2 + 1, (ey + sy) // 2 + 1, ex, ey)


z(0, 0, 0, 2**N - 1, 2**N - 1)

print(answer)
