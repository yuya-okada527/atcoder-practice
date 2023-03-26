n, s = map(int, input().split())
A = [0] + list(map(int, input().split()))
DP = [[False for _ in range(s+1)] for _ in range(n+1)]
DP[0][0] = True
for i in range(n+1):
    for j in range(s+1):
        if DP[i-1][j]: DP[i][j] = True
        else:
            if j - A[i] < 0: continue
            if DP[i-1][j-A[i]]: DP[i][j] = True
if not DP[-1][-1]:
    print(-1)
    exit()
current = s
path = []
for i in range(n, 0, -1):
    if DP[i-1][current]: continue
    else:
        current -= A[i]
        path.append(i)
print(len(path))
print(*path[::-1], sep=" ")
