n = int(input())
a = list(map(int, input().split()))

d = [0] * n
d[0] = 1

for i in range(1, n):
    max_n = 0
    for j in range(i-1, -1, -1):

        if a[j] > a[i] and d[j] > max_n:
            max_n = d[j]
    d[i] = max_n + 1

print(max(d))
