n, s = map(int, input().split())
A = [0] + list(map(int, input().split()))
DP = [[False for _ in range(s+1)] for _ in range(n+1)]
for i in range(n+1):
    for j in range(s+1):
        if i == 0 and j == 0: DP[i][j] = True
        elif i == 0: DP[i][j] = False
        elif DP[i-1][j]: DP[i][j] = True
        elif j >= A[i]:
            if DP[i-1][j-A[i]]:
                DP[i][j] = True
if DP[-1][-1]: print("Yes")
else: print("No")
