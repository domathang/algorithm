n, k = map(int, input().split())
values = [int(input()) for i in range(n)]
values.sort(reverse=True)
cnt = 0
for i in values:
    cnt += k // i
    k %= i
print(cnt)
