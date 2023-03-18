from pprint import pprint

n, s = map(int, input().split())
A = [0] + list(map(int, input().split()))
DP = [[False for _ in range(s+1)] for _ in range(n+1)]
DP[0][0] = True
for i in range(1, n+1):
    for j in range(s+1):
        DP[i][j] = DP[i-1][j] or (j >= A[i] and DP[i-1][j-A[i]])
if not DP[-1][-1]:
    print(-1)
    exit()
pos = s
path = []
for i in range(n, 0, -1):
    if DP[i-1][pos]: continue
    else:
        path.append(i)
        pos -= A[i]
print(len(path))
print(*path[::-1], sep=" ")
