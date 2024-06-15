n = int(input())
dp = [-1, -1, 1, -1, 1] + [-1] * 4995
for i in range(5, n):
    i3 = dp[i-3] if dp[i-3] != -1 else -1
    i5 = dp[i-5] if dp[i-5] != -1 else -1
    if i3 == i5 == -1:
        dp[i] = -1
    elif i3 == -1 or i5 == -1:
        dp[i] = max(dp[i-3], dp[i-5]) + 1
    else:
        dp[i] = min(dp[i-3], dp[i-5]) + 1
print(dp[n-1])
