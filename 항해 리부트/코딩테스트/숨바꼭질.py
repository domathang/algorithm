n, k = map(int, input().split())
q = [(n, 0)]
answer = 100001
check = [0] * 200000
while q:
    p = q.pop(0)
    cur = p[0]
    if cur == k:
        answer = min(answer, p[1])
    elif cur > k:
        answer = min(answer, p[1] + cur - k)
    else:
        if cur < 100000:
            if check[cur * 2] == 0:
                q.append((cur * 2, p[1] + 1))
                check[cur * 2] = 1
        if cur > 1:
            if check[cur - 1] == 0:
                q.append((cur - 1, p[1] + 1))
                check[cur - 1] = 1
        if check[cur + 1] == 0:
            q.append((cur + 1, p[1] + 1))
            check[cur + 1] = 1
print(answer)
