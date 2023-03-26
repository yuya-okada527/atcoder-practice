from pprint import pprint

SIZE = 1509
SPACE = [[0 for _ in range(SIZE+1)] for _ in range(SIZE+1)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    SPACE[y][x] += 1
Z = [[0 for _ in range(SIZE+1)] for _ in range(SIZE+1)]
for i in range(SIZE+1):
    for j in range(SIZE+1):
        Z[i][j] = Z[i-1][j] + SPACE[i][j]
for i in range(SIZE+1):
    for j in range(SIZE+1):
        Z[i][j] = Z[i][j-1] + Z[i][j]
q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    ans = Z[d][c] - Z[d][a-1] - Z[b-1][c] + Z[b-1][a-1]
    print(ans)
