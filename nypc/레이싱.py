n, m = map(int, input().split())
log = [list(map(int, input().split())) for x in range(m)]
user = [-1 for i in range(n+1)]
time = [0 for i in range(n+1)]
answer = "YES"
for t, i, s in log:
    if s == 0:
        if user[i] == 0:
            answer = "NO"
            break
        else:
            user[i] = 0
            time[i] = t
    elif s == 1:
        if user[i] == 0:
            if t - time[i] < 60:
                answer = "NO"
                break
            user[i] = 1
        else:
            answer = "NO"
            break
for i in user:
    if i == 0:
        answer = "NO"
        break
print(answer)
