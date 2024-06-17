n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0
for i in coins[::-1]:
    cnt += k // i
    k %= i
print(cnt)
