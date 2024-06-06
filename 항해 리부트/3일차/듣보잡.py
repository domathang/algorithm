n, m = map(int, input().split())
dd = []
answer = []
for i in range(n+m-1):
    dd.append(input())
dd.sort()
for i in range(1, len(dd)):
    if dd[i] == dd[i-1]:
        answer.append(dd[i])
print(len(answer))
print(*answer, sep="\n")