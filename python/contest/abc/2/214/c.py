
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

dp = [T[0]] + [10*9+1 for _ in range(N-1)]
for i in range(N):
    dp[i] = min(T[i], dp[i-1] + S[i-1])

dp[0] = min(T[0], dp[N-1] + S[i-1])
for i in range(N):
    dp[i] = min(T[i], dp[i-1] + S[i-1])

for ans in dp:
    print(ans)