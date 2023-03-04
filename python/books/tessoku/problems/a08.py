from pprint import pprint as print

h, w = map(int, input().split())
X = [[0 for _ in range(w+2)] for _ in range(h+2)]
for i in range(1, h+1):
    for j, x in enumerate(map(int, input().split()), start=1):
        X[i][j] = x
Z = [[0 for _ in range(w+2)] for _ in range(h+2)]
for i in range(1, h+1):
    for j in range(1, w+1):
        Z[i][j] = Z[i-1][j] + X[i][j]
for i in range(1, h+1):
    for j in range(1, w+1):
        Z[i][j] = Z[i][j-1] + Z[i][j]
q = int(input())
Q = []
for _ in range(q):
    a, b, c, d = map(int, input().split())
    Q.append((a, b, c, d))
# print(Z)
for a, b, c, d in Q:
    ans = Z[c][d] - Z[a-1][d] - Z[c][b-1] + Z[a-1][b-1]
    print(ans)
