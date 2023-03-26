n, s = map(int, input().split())
A = [0] + list(map(int, input().split()))
DP = [[False for _ in range(s+1)] for _ in range(n+1)]
DP[0][0] = True
for i in range(1, n+1):
    for j in range(s+1):
        if DP[i-1][j]: DP[i][j] = True
        else:
            if j - A[i] < 0:
                continue
            if DP[i-1][j-A[i]]: DP[i][j] = True
if DP[-1][-1]: print("Yes")
else: print("No")
