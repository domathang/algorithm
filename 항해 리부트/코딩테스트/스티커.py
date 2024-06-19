t = int(input())
for _ in range(t):
    n = int(input())
    stickers = [list(map(int,input().split())) for _ in range(2)]

    dp = [[0]*3 for _ in range(n)]
    dp[0][1] = stickers[0][0]
    dp[0][2] = stickers[1][0]

    for i in range(1,n):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + stickers[0][i]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + stickers[1][i]
    print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))