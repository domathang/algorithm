n, k = map(int, input().split())
day = list(map(int, input().split()))
days = [[i+1, day[i]] for i in range(len(day))]
max_person = list(map(int, input().split()))
worktable = []

for m in range(k):
    days = sorted(days, key=lambda x: x[1], reverse=True)
    a = []
    for d in days[0:max_person[m]]:
        if d[1] > 0:
            d[1] -= 1
            a.append(d[0])
    worktable.append(a)

for i in worktable:
    print(str(len(i)) + " ", end='')
    print(" ".join(list(map(str, i))))
