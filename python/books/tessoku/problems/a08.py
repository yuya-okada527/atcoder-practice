h, w = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
Q = [list(map(int, input().split())) for _ in range(q)]

CUMS = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i == 0: CUMS[i][j] = X[i][j]
        else: CUMS[i][j] = CUMS[i-1][j] + X[i][j]
for a, b, c, d in Q:
    a_row = CUMS[a-2] if a != 1 else [0 for _ in range(w)]
    c_row = CUMS[c-1]
    a_row_column = a_row[b-1:d] if d != w else a_row[b-1:]
    c_row_column = c_row[b-1:d] if d != w else c_row[b-1:]
    print(sum(c_row_column) - sum(a_row_column))
