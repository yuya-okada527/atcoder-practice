h, w, n = map(int, input().split())
DIFF = [[0 for _ in range(w+9)] for _ in range(h+9)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    DIFF[b][a] += 1
    DIFF[d+1][a] -= 1
    DIFF[b][c+1] -= 1
    DIFF[d+1][c+1] += 1
Z = [[0 for _ in range(w+9)] for _ in range(h+9)]
for x in range(1, w+1):
    for y in range(1, h+1):
        Z[y][x] = Z[y][x-1] + DIFF[y][x]
for x in range(1, w+1):
    for y in range(1, h+1):
        Z[y][x] = Z[y-1][x] + Z[y][x]
for x in range(1, h+1):
    print(" ".join(map(str, Z[x][1:w+1])))
