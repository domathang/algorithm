n = int(input())
dp = ["SK", "CY", "SK"] + [""] * 1000
for i in range(3, n):
    if dp[i - 3] == "SK":
        dp[i] = "CY"
    else:
        dp[i] = "SK"
print(dp[n-1])