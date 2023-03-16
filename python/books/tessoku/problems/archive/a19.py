# from pprint import pprint

n, w = map(int, input().split())
W = [0]
V = [0]
for _ in range(n):
    weight, value = map(int, input().split())
    W.append(weight)
    V.append(value)
DP = [[-1 for _ in range(w+1)] for _ in range(n+1)]
for i in range(n+1):
    for j in range(w+1):
        if i == 0 and j == 0: DP[i][j] = 0
        elif i == 0: DP[i][j] = -1
        elif j >= W[i]:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-W[i]] + V[i])
        else:
            DP[i][j] = DP[i-1][j]
# pprint(DP)
print(max(DP[-1]))
