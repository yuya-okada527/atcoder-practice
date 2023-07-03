h, w = map(int, input().split())
X = [[0 for _ in range(w+1)] for _ in range(h+1)]
C = [[0 for _ in range(w+1)] for _ in range(h+1)]
for i in range(1, h+1):
    for j, x in enumerate(input().split(), start=1):
        X[i][j] = int(x)
for i in range(1, h+1):
    for j in range(1, w+1):
        C[i][j] = C[i][j-1] + X[i][j]
for i in range(1, h+1):
    for j in range(1, w+1):
        C[i][j] = C[i-1][j] + C[i][j]
Q = [map(int, input().split()) for _ in range(int(input()))]
for a, b, c, d in Q:
    ans = C[c][d] - C[a-1][d] - C[c][b-1] + C[a-1][b-1]
    print(ans)
