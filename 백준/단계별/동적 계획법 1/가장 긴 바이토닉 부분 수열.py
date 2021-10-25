n = int(input())
a = list(map(int, input().split()))

d1 = [0] * n
d2 = [0] * n
d1[0] = 1
d2[n-1] = 1

for i in range(1, n):
    max_n = 0
    for j in range(0, i):

        if a[j] < a[i] and d1[j] > max_n:
            max_n = d1[j]
    d1[i] = max_n + 1

for i in range(n-2, -1, -1):
    max_n = 0
    for j in range(i+1, n):

        if a[j] < a[i] and d2[j] > max_n:
            max_n = d2[j]
    d2[i] = max_n + 1

answer = 0

for i in range(0, n):
    if answer < d1[i] + d2[i]:
        answer = d1[i] + d2[i]

print(answer-1)
