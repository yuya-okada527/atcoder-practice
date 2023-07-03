h, w = map(int, input().split())
HW = [[0 for _ in range(w+1)] for _ in range(h+1)]
for i in range(1, h+1):
    for j, v in enumerate(map(int, input().split()), start=1):
        HW[i][j] = v
Z = [[0 for _ in range(w+1)] for _ in range(h+1)]
for i in range(1, h+1):
    for j in range(1, w+1):
        Z[i][j] = Z[i-1][j] + HW[i][j]
for i in range(1, h+1):
    for j in range(w+1):
        Z[i][j] = Z[i][j-1] + Z[i][j]
q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    ans = Z[c][d] - Z[c][b-1] - Z[a-1][d] + Z[a-1][b-1]
    print(ans)
