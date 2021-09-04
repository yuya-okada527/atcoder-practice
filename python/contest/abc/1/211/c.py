S = input()
T = "chokudai"
dp = [[0 for _ in range(8+1)] for _ in range(len(S)+1)]

for i in range(len(S)+1):
    for j in range(8+1):
        if j == 0:
            dp[i][j] = 1
        elif i == 0:
            dp[i][j] = 0
        elif S[i-1] != T[j-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[len(S)][8] % (10**9+7))
