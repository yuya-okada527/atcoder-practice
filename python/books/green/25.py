N = int(input())
H = list(map(int, input().split()))
dp = [0] * N
for i in range(N):
    if i == 0:
        continue
    elif i == 1:
        dp[i] = abs(H[0]-H[1])
    else:
        dp[i] = min(dp[i-1]+abs(H[i-1]-H[i]), dp[i-2]+abs(H[i-2]-H[i]))
print(dp[N-1])
