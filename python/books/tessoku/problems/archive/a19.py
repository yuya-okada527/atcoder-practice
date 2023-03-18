n, w = map(int, input().split())
W = [0]
V = [0]
for _ in range(n):
    weight, value = map(int, input().split())
    W.append(weight)
    V.append(value)
DP = [[-10**10 for _ in range(w+1)] for _ in range(n+1)]
for i in range(n+1):
    for j in range(w+1):
        if i == j == 0: DP[i][j] = 0
        elif i == 0: continue
        else:
            if W[i] > j: DP[i][j] = DP[i-1][j]
            else: DP[i][j] = max(DP[i-1][j], DP[i-1][j-W[i]]+V[i])
print(max(DP[-1]))
