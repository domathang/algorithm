n = int(input())

exes = {}

for i in range(n):
    ex = input().split('.')[1]
    if ex in exes:
        exes[ex] += 1
    else:
        exes[ex] = 1

res = []

for k in exes:
    res.append((k, exes[k]))

res.sort()

for k, v in res:
    print(f"{k} {v}")
