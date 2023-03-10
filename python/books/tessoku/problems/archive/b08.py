from pprint import pprint as print
SIZE = 1502

n = int(input())
X = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
for _ in range(n):
    x, y = map(int, input().split())
    X[x][y] += 1
Z = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
for i in range(1, SIZE-1):
    for j in range(1, SIZE-1):
        Z[i][j] = Z[i-1][j] + X[i][j]
for i in range(1, SIZE-1):
    for j in range(1, SIZE-1):
        Z[i][j] = Z[i][j-1] + Z[i][j]
q = int(input())
Q = []
for _ in range(q):
    a, b, c, d = map(int, input().split())
    Q.append((a, b, c, d))
for a, b, c, d in Q:
    ans = Z[c][d] - Z[a-1][d] - Z[c][b-1] + Z[a-1][b-1]
    print(ans)
