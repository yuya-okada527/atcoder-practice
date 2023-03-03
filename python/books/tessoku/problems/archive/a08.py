h, w = map(int, input().split())
X = [[0 for _ in range(w+9)] for _ in range(h+9)]
for i in range(1, h+1):
    line = list(map(int, input().split()))
    for j in range(1, w+1):
        X[i][j] = line[j]
q = int(input())
Q = [list(map(int, input().split())) for _ in range(q)]

CUMS = [[0 for _ in range(w+9)] for _ in range(h+9)]
for i in range(1, h+1):
    for j in range(1, w+1):
        CUMS[i][j] = CUMS[i-1][j] + X[i][j]
for i in range(1, h+1):
    for j in range(1, w+1):
        CUMS[i][j] = CUMS[i][j-1] + CUMS[i][j]
print(CUMS)
for a, b, c, d in Q:
    print(CUMS[c][d] + CUMS[a-1][b-1] - CUMS[a][d-1] - CUMS[b-1][c])
