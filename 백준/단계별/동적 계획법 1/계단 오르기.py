n = int(input())
stair = [int(input()) for _ in range(n)]

dp = [[0, 0, 0] for i in range(n+10)]

dp[0][1] = stair[0]
if n != 1:
    dp[1][1] = stair[1]
    dp[1][2] = dp[0][1] + stair[1]

for i in range(2, n):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stair[i]
    dp[i][2] = dp[i-1][1] + stair[i]


print(max(dp[n-1][1], dp[n-1][2]))
