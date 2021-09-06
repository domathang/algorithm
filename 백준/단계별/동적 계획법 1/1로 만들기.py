x = int(input())
dp = [0 for _ in range(10000000)]

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[int(i/2)] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[int(i/3)] + 1)
print(dp[x])