n, m = map(int, input().split())
target = list(map(int, input().split()))
q = [i for i in range(1, n+1)]
answer = 0


for i in target:
    cnt = 0
    e = q.index(i)
    while q[0] != i:
        cnt += 1
        if e < len(q) - e + 1:
            q.append(q.pop(0))
        else:
            q.insert(0, q.pop())
    q.pop(0)
    answer += cnt
print(answer)
