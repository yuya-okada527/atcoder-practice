SIZE = 1500 + 2
n = int(input())
XY = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
C = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
for _ in range(n):
    x, y = map(int, input().split())
    XY[x][y] += 1
for i in range(1, SIZE-1):
    for j in range(1, SIZE-1):
        C[i][j] = C[i-1][j] + XY[i][j]
for i in range(1, SIZE-1):
    for j in range(1, SIZE-1):
        C[i][j] = C[i][j-1] + C[i][j]
Q = [map(int, input().split()) for _ in range(int(input()))]
for a, b, c, d in Q:
    ans = C[c][d] - C[a-1][d] - C[c][b-1] + C[a-1][b-1]
    print(ans)
