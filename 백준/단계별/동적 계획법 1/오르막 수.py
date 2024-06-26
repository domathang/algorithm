n = int(input())
dp = [[0 for i in range(10)] for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j] % 10007
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 10007
answer = sum([dp[n][i] for i in range(10)])
print(answer % 10007)