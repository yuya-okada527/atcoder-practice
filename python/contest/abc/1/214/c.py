N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# 1週目を考える
dp = [T[0]] + [10**10 for _ in range(N-1)]
for i in range(N):
    # 高橋くんから直接もらう場合か、１つ前のすぬけ君からもらう場合のどちらが早いか計算する
    dp[i] = min(T[i], dp[i-1] + S[i-1])

# 2週目を考える
# N番目から、1番目へ渡す場合を考慮する
dp[0] = min(dp[0], dp[N-1] + S[N-1])
for i in range(N):
    dp[i] = min(T[i], dp[i-1] + S[i-1])

for ans in dp:
    print(ans)