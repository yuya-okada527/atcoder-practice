n, w = map(int, input().split())
W, V = [0], [0]
for _ in range(n):
    weight, value = map(int, input().split())
    W.append(weight)
    V.append(value)
DP = [[-10**11 for _ in range(w+1)] for _ in range(n+1)]
DP[0][0] = 0
for i in range(1, n+1):
    for j in range(w+1):
        if j - W[i] >= 0:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-W[i]]+V[i])
        else:
            DP[i][j] = DP[i-1][j]
print(max(DP[-1]))
