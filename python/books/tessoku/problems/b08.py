N_DIM = 1509
n = int(input())
XY = [[0 for _ in range(N_DIM)] for _ in range(N_DIM)]
for _ in range(n):
    x, y = map(int, input().split())
    XY[x][y] += 1
Z = [[0 for _ in range(N_DIM)] for _ in range(N_DIM)]
for x in range(1, N_DIM):
    for y in range(1, N_DIM):
        Z[x][y] = Z[x-1][y] + XY[x][y]
for x in range(1, N_DIM):
    for y in range(1, N_DIM):
        Z[x][y] = Z[x][y-1] + Z[x][y]
q = int(input())
Q = [list(map(int, input().split())) for _ in range(q)]
for a, b, c, d in Q:
    ans = Z[c][d] - Z[c][b-1] - Z[a-1][d] + Z[a-1][b-1]
    print(ans)
