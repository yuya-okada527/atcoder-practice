from pprint import pprint
s = "x" + input()
t = "x" + input()
DP = [[0 for _ in range(len(t))] for _ in range(len(s))]
for i in range(len(s)):
    for j in range(len(t)):
        if i == 0: continue
        if j == 0: DP[i][j] = DP[i-1][j]
        else:
            if s[i] == t[j]:
                DP[i][j] = max(
                    DP[i-1][j],    # 上から
                    DP[i][j-1],    # 左から
                    DP[i-1][j-1]+1 # ななめ
                )
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
print(DP[-1][-1])
