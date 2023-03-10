SIZE = 1502

n = int(input())
XY = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
for _ in range(n):
    x, y = map(int, input().split())
    XY[x][y] += 1
Z = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
for i in range(1, SIZE-1):
    for j in range(1, SIZE-1):
        Z[i][j] = Z[i-1][j] + XY[i][j]
for i in range(1, SIZE-1):
    for j in range(1, SIZE-1):
        Z[i][j] = Z[i][j-1] + Z[i][j]
q = int(input())
Q = [map(int, input().split()) for _ in range(q)]
for a, b, c, d in Q:
    ans = Z[c][d] - Z[a-1][d] - Z[c][b-1] + Z[a-1][b-1]
    print(ans)
